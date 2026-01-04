#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Dict, List, Tuple, Optional
from datetime import date, datetime, timedelta, timezone
import requests, time, csv, json, math
from pathlib import Path

API_BASE = "https://ucdpapi.pcr.uu.se/api"
GED_YEAR_VERSION = "25.1"                 # årsrelease (t.o.m. 2024-12-31)
PAGE_SIZE = 1000
TIMEOUT = 30
RETRIES = 4
BACKOFF = 2.0
OUT_CSV  = "sec_conflicts.csv"

START = datetime.strptime("2017-01-01", "%Y-%m-%d").date()
END = datetime.strptime("2017-12-31", "%Y-%m-%d").date()


# Valfritt filter, ex: {"TypeOfViolence": 1} (1=state-based, 2=non-state, 3=one-sided)
OPTIONAL_FILTERS: Dict[str, int | str] = {}

@dataclass
class Row:
    source_type: str        # "candidate" | "ged"
    source_version: str     # ex "25.0.9" eller "25.1"
    period_type: str        # "month" | "year"
    period_label: str       # "YYYY-MM" | "YYYY"
    start_date: str
    end_date: str
    events_count: int
    conflicts_count: int
    deaths_best_sum: int
    deaths_best_per_conflict: float
    note: Optional[str] = None  # ex "(saknas)"

# --- Datumhjälp ---
def first_of_month(d: date) -> date: return d.replace(day=1)
def last_of_month(d: date) -> date:
    nm = d.replace(day=28) + timedelta(days=4)
    return nm - timedelta(days=nm.day)

def add_months(d: date, m: int) -> date:
    y = d.year + (d.month - 1 + m)//12
    mo = (d.month - 1 + m)%12 + 1
    day = min(d.day, [31,29 if (y%4==0 and (y%100!=0 or y%400==0)) else 28,31,30,31,30,31,31,30,31,30,31][mo-1])
    return date(y, mo, day)

def months(START: date, END: date) -> List[Tuple[str,str,str,int,int]]:
    start = first_of_month(START)
    end = last_of_month(END)
    out = []
    cur = start
    while cur <= end:
        start_m = first_of_month(cur)
        end_m = last_of_month(cur)
        out.append((start_m.strftime("%Y-%m"), start_m.isoformat(), end_m.isoformat(), start_m.year, start_m.month))
        cur = add_months(cur, +1)
    return out

# --- Version-mappning för Candidate ---
def candidate_version_for(year: int, month: int) -> str:
    """
    UCDP Candidate versioneras 'YY.0.M' per kalendermånad.
    Ex: 2025-09 -> 25.0.9, 2024-12 -> 24.0.12
    """
    yy = year % 100
    return f"{yy}.0.{month}"

# --- API ---
def get_with_retries(url: str, params: Dict[str, str | int]) -> dict:
    for i in range(1, RETRIES+1):
        try:
            r = requests.get(url, params=params, timeout=TIMEOUT)
            # 404 betraktas som "saknas" för månadsutgåvor
            if r.status_code == 404:
                return {"Result": [], "TotalPages": 0, "TotalCount": 0, "_status": 404}
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            if i == RETRIES:
                raise
            time.sleep(BACKOFF * i)
    return {"Result": []}

def fetch_events(resource_version: str, start_date: str, end_date: str) -> dict:
    url = f"{API_BASE}/gedevents/{resource_version}"
    params = {"pagesize": PAGE_SIZE, "StartDate": start_date, "EndDate": end_date, **OPTIONAL_FILTERS}
    page = 0
    all_events = []
    while True:
        data = get_with_retries(url, {**params, "page": page})
        result = data.get("Result", [])
        status = data.get("_status")
        if status == 404:
            return {"events": [], "status": 404}
        all_events.extend(result)
        total_pages = data.get("TotalPages", None)
        if not result or (total_pages is not None and page >= total_pages - 1):
            return {"events": all_events, "status": 200}
        page += 1

# --- Aggregat ---
def summarize(events: List[dict]) -> Tuple[int,int,int,float]:
    conflicts, deaths = set(), 0
    for e in events:
        cid = e.get("conflict_new_id")
        if cid is not None:
            conflicts.add(cid)
        best = e.get("best")
        if isinstance(best, (int, float)) and not math.isnan(best):
            deaths += int(best)
    c_cnt = len(conflicts)
    return len(events), c_cnt, deaths, round(deaths / c_cnt, 2) if c_cnt else 0.0

# --- Körning ---
def main():
    rows: List[Row] = []

    for label, start, end, y, m in months(START, END):
        print(f"Hämtar GED {GED_YEAR_VERSION} för {label}, {start} - {end} med y={y}, m={m}")
        cand_ver = candidate_version_for(y, m)
        fetched = fetch_events(cand_ver, start, end)
        if fetched["status"] == 404 or len(fetched["events"]) == 0:
            rows.append(Row("candidate", cand_ver, "month", label, start, end, 0, 0, 0, 0.0, note="(saknas)"))
            print("  Saknas")
        else:
            e_cnt, c_cnt, d_sum, d_per = summarize(fetched["events"])
            rows.append(Row("candidate", cand_ver, "month", label, start, end, e_cnt, c_cnt, d_sum, d_per))
            print(f"Month {label}:  conflicts={c_cnt}, deaths={d_sum}")

    out_csv  = Path(OUT_CSV)
    
    cols = ["source_type","source_version","period_type","period_label","start_date","end_date",
            "events_count","conflicts_count","deaths_best_sum","deaths_best_per_conflict","note"]
    with out_csv.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        if f.tell() == 0: w.writeheader()
        for r in rows:
            w.writerow(asdict(r))

    print(f"\nSparat: {OUT_CSV}")

if __name__ == "__main__":
    main()
 