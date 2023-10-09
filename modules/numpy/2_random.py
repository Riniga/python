from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("- Random -----------------")
rand_int = random.randint(100)
rand_float = random.rand()
rand_arr=random.randint(100, size=(5))
rand_twoD_array = random.rand(3, 5)
rand_pocked_from_list = random.choice([3, 5, 7, 9])
rand_twoD_array_from_list = random.choice([True, False], size=(3, 5))
print(rand_twoD_array_from_list)

class Distributions():
    def randomdatadistribution(self):
        print("- Random Data Distribution -----------------")
        rand_from_list_distributed = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
        print(rand_from_list_distributed)

    def randompermutations(self):
        print("- Random Permutations -----------------")
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = arr1.copy()
        random.shuffle(arr1)
        print(arr1)
        permutations = random.permutation(arr2)
        print(permutations)

    def seaborn(self):
        print("- Seaborn -----------------")
        sns.distplot([0, 1, 2, 3, 4, 5])
        sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
        plt.show()
    
    def normaldistribution(self):
        print("- Normal Distribution -----------------")
        x = random.normal(size=(2, 3))
        x = random.normal(loc=1, scale=2, size=(2, 3))
        sns.distplot(x)
        print(x)
        plt.show()

    def binomialdistribution(self):
        print("- Binomial Distribution -----------------")
        sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
        sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
        plt.legend(title = "Distributions:")
        plt.show()
    
    def poissondistribution(self):
        sns.distplot(random.poisson(lam=2, size=1000), kde=False, label="poisson")
        plt.show()

    def uniformdistribution(self):
        sns.distplot(random.uniform(size=1000), hist=False, label='uniform')
        plt.show()

    def logisticdistribution(self):
        sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
        sns.distplot(random.logistic(size=1000), hist=False,  label='logistic')
        plt.legend(title = "Distributions:")
        plt.title("Logistic Distribution is used to describe growth.")
        plt.text(-7,0.1, "Used extensively in machine learning in logistic regression, \nneural networks etc.")
        plt.show()

    def multinomialdistribution(self):
        print("- Multinomial Distribution -----------------")
        x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
        print(x)

    def exponentialdistribution(self):
        sns.distplot(random.exponential(size=1000), hist=False)
        plt.title("Exponential Distribution")
        plt.text(2,0.5, "Exponential distribution is used \nfor describing time till next event \ne.g. failure/success etc.")
        plt.show()

    def chisquaredistribution(self):
        print("- Chi Square Distribution -----------------")
        x = random.chisquare(df=2, size=(2, 3))
        print(x)
        sns.distplot(random.chisquare(df=1, size=1000), hist=False)
        plt.title("Chi Square Distribution")
        plt.text(3,0.5, "Chi Square distribution is used as \na basis to verify the hypothesis.")
        plt.show()

    def rayleigh(self):
        print("- Rayleigh Distribution -----------------")
        x = random.rayleigh(scale=2, size=(2, 3))
        print(x)
        sns.distplot(random.rayleigh(size=1000), hist=False)
        plt.title("Rayleigh Distribution")
        plt.text(0,0.4, "Rayleigh distribution is used in signal processing.")
        plt.show()
    
    def paretodistribution(self):
        print("- Pareto Distribution -----------------")
        x = random.pareto(a=2, size=(2, 3))
        print(x)
        sns.distplot(random.pareto(a=2, size=1000), kde=False)
        plt.title("Pareto Distribution")
        plt.text(10,200, "A distribution following Pareto's law \ni.e. 80-20 distribution \n(20% factors cause 80% outcome).")
        plt.show()

    def zipfdistribution(self):
        print("- Zipf  Distribution -----------------")
        x = random.zipf(a=2, size=(2, 3))
        print(x)
        x = random.zipf(a=2, size=1000)
        sns.distplot(x[x<10], kde=False)
        plt.title("Zipf  Distribution")
        plt.text(2,200, "Zipf distributions are used to \nsample data based on zipf's law.")
        plt.show()

distributions = Distributions()
distributions.zipfdistribution()
