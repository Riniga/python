var _JUPYTERLAB;(()=>{"use strict";var e,r,t,o,n,a,i,u,l,s,d,f,p,c,v,h,b,y,g,m,w,j,S={85:(e,r,t)=>{var o={"./index":()=>t.e(235).then((()=>()=>t(235))),"./extension":()=>t.e(235).then((()=>()=>t(235))),"./style":()=>t.e(643).then((()=>()=>t(643)))},n=(e,r)=>(t.R=r,r=t.o(o,e)?o[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),a=(e,r)=>{if(t.S){var o="default",n=t.S[o];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[o]=e,t.I(o,r)}};t.d(r,{get:()=>n,init:()=>a})}},k={};function E(e){var r=k[e];if(void 0!==r)return r.exports;var t=k[e]={id:e,exports:{}};return S[e](t,t.exports,E),t.exports}E.m=S,E.c=k,E.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return E.d(r,{a:r}),r},E.d=(e,r)=>{for(var t in r)E.o(r,t)&&!E.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},E.f={},E.e=e=>Promise.all(Object.keys(E.f).reduce(((r,t)=>(E.f[t](e,r),r)),[])),E.u=e=>e+"."+{235:"f37eb34a25a67c6a0bd8",643:"fea2c78a397c78fca01c"}[e]+".js?v="+{235:"f37eb34a25a67c6a0bd8",643:"fea2c78a397c78fca01c"}[e],E.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),E.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="@voila-dashboards/jupyterlab-preview:",E.l=(t,o,n,a)=>{if(e[t])e[t].push(o);else{var i,u;if(void 0!==n)for(var l=document.getElementsByTagName("script"),s=0;s<l.length;s++){var d=l[s];if(d.getAttribute("src")==t||d.getAttribute("data-webpack")==r+n){i=d;break}}i||(u=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,E.nc&&i.setAttribute("nonce",E.nc),i.setAttribute("data-webpack",r+n),i.src=t),e[t]=[o];var f=(r,o)=>{i.onerror=i.onload=null,clearTimeout(p);var n=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(o))),r)return r(o)},p=setTimeout(f.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=f.bind(null,i.onerror),i.onload=f.bind(null,i.onload),u&&document.head.appendChild(i)}},E.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{E.S={};var e={},r={};E.I=(t,o)=>{o||(o=[]);var n=r[t];if(n||(n=r[t]={}),!(o.indexOf(n)>=0)){if(o.push(n),e[t])return e[t];E.o(E.S,t)||(E.S[t]={});var a=E.S[t],i="@voila-dashboards/jupyterlab-preview",u=[];return"default"===t&&((e,r,t,o)=>{var n=a[e]=a[e]||{},u=n[r];(!u||!u.loaded&&(1!=!u.eager?o:i>u.from))&&(n[r]={get:()=>E.e(235).then((()=>()=>E(235))),from:i,eager:!1})})("@voila-dashboards/jupyterlab-preview","2.3.4"),e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;E.g.importScripts&&(e=E.g.location+"");var r=E.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var o=t.length-1;o>-1&&!e;)e=t[o--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),E.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),o=t[1]?r(t[1]):[];return t[2]&&(o.length++,o.push.apply(o,r(t[2]))),t[3]&&(o.push([]),o.push.apply(o,r(t[3]))),o},o=(e,r)=>{e=t(e),r=t(r);for(var o=0;;){if(o>=e.length)return o<r.length&&"u"!=(typeof r[o])[0];var n=e[o],a=(typeof n)[0];if(o>=r.length)return"u"==a;var i=r[o],u=(typeof i)[0];if(a!=u)return"o"==a&&"n"==u||"s"==u||"u"==a;if("o"!=a&&"u"!=a&&n!=i)return n<i;o++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var o=1,a=1;a<e.length;a++)o--,t+="u"==(typeof(u=e[a]))[0]?"-":(o>0?".":"")+(o=2,u);return t}var i=[];for(a=1;a<e.length;a++){var u=e[a];i.push(0===u?"not("+l()+")":1===u?"("+l()+" || "+l()+")":2===u?i.pop()+" "+i.pop():n(u))}return l();function l(){return i.pop().replace(/^\((.+)\)$/,"$1")}},a=(e,r)=>{if(0 in e){r=t(r);var o=e[0],n=o<0;n&&(o=-o-1);for(var i=0,u=1,l=!0;;u++,i++){var s,d,f=u<e.length?(typeof e[u])[0]:"";if(i>=r.length||"o"==(d=(typeof(s=r[i]))[0]))return!l||("u"==f?u>o&&!n:""==f!=n);if("u"==d){if(!l||"u"!=f)return!1}else if(l)if(f==d)if(u<=o){if(s!=e[u])return!1}else{if(n?s>e[u]:s<e[u])return!1;s!=e[u]&&(l=!1)}else if("s"!=f&&"n"!=f){if(n||u<=o)return!1;l=!1,u--}else{if(u<=o||d<f!=n)return!1;l=!1}else"s"!=f&&"n"!=f&&(l=!1,u--)}}var p=[],c=p.pop.bind(p);for(i=1;i<e.length;i++){var v=e[i];p.push(1==v?c()|c():2==v?c()&c():v?a(v,r):!c())}return!!c()},i=(e,r)=>{var t=E.S[e];if(!t||!E.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},u=(e,r)=>{var t=e[r];return(r=Object.keys(t).reduce(((e,r)=>!e||o(e,r)?r:e),0))&&t[r]},l=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&o(e,r)?r:e),0)},s=(e,r,t,o)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+n(o)+")",d=(e,r,t,o)=>{var n=l(e,t);return a(o,n)||c(s(e,t,n,o)),h(e[t][n])},f=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!a(t,r)||e&&!o(e,r)?e:r),0))&&n[r]},p=(e,r,t,o)=>{var a=e[t];return"No satisfying version ("+n(o)+") of shared module "+t+" found in shared scope "+r+".\nAvailable versions: "+Object.keys(a).map((e=>e+" from "+a[e].from)).join(", ")},c=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},v=(e,r,t,o)=>{c(p(e,r,t,o))},h=e=>(e.loaded=1,e.get()),y=(b=e=>function(r,t,o,n){var a=E.I(r);return a&&a.then?a.then(e.bind(e,r,E.S[r],t,o,n)):e(r,E.S[r],t,o,n)})(((e,r,t,o)=>(i(e,t),h(f(r,t,o)||v(r,e,t,o)||u(r,t))))),g=b(((e,r,t,o)=>(i(e,t),d(r,0,t,o)))),m={},w={29:()=>g("default","react",[1,18,2,0]),57:()=>g("default","@jupyterlab/ui-components",[1,4,0,6]),65:()=>g("default","@jupyterlab/coreutils",[1,6,0,6]),119:()=>g("default","@jupyterlab/apputils",[1,4,1,6]),445:()=>g("default","@jupyterlab/application",[1,4,0,6]),460:()=>y("default","@jupyterlab/docregistry",[1,4,0,6]),680:()=>g("default","@jupyterlab/settingregistry",[1,4,0,6]),777:()=>g("default","@jupyterlab/mainmenu",[1,4,0,6]),829:()=>g("default","@jupyterlab/notebook",[1,4,0,6]),901:()=>g("default","@lumino/signaling",[1,2,0,0]),930:()=>g("default","@lumino/coreutils",[1,2,0,0])},j={235:[29,57,65,119,445,460,680,777,829,901,930]},E.f.consumes=(e,r)=>{E.o(j,e)&&j[e].forEach((e=>{if(E.o(m,e))return r.push(m[e]);var t=r=>{m[e]=0,E.m[e]=t=>{delete E.c[e],t.exports=r()}},o=r=>{delete m[e],E.m[e]=t=>{throw delete E.c[e],r}};try{var n=w[e]();n.then?r.push(m[e]=n.then(t).catch(o)):t(n)}catch(e){o(e)}}))},(()=>{var e={329:0};E.f.j=(r,t)=>{var o=E.o(e,r)?e[r]:void 0;if(0!==o)if(o)t.push(o[2]);else{var n=new Promise(((t,n)=>o=e[r]=[t,n]));t.push(o[2]=n);var a=E.p+E.u(r),i=new Error;E.l(a,(t=>{if(E.o(e,r)&&(0!==(o=e[r])&&(e[r]=void 0),o)){var n=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+a+")",i.name="ChunkLoadError",i.type=n,i.request=a,o[1](i)}}),"chunk-"+r,r)}};var r=(r,t)=>{var o,n,[a,i,u]=t,l=0;if(a.some((r=>0!==e[r]))){for(o in i)E.o(i,o)&&(E.m[o]=i[o]);u&&u(E)}for(r&&r(t);l<a.length;l++)n=a[l],E.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunk_voila_dashboards_jupyterlab_preview=self.webpackChunk_voila_dashboards_jupyterlab_preview||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),E.nc=void 0;var _=E(85);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@voila-dashboards/jupyterlab-preview"]=_})();