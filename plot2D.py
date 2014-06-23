from pylab import *
from numpy import *
from scipy import *
from scipy import optimize
from subprocess import call
import sys

def add_plot(path):

# Load data
    x,y = loadtxt(path,unpack=True, usecols=[0,1], skiprows=1)


# Label PLot
    title = "Pseudo plot"
    xxis  = "Independant variable"
    yxis  = "Dependant variable"
    ax.set_title(title)
    ax.set_xlabel(xxis)
    ax.set_ylabel(yxis)
    
    ax.plot(x,y, alpha=.8, label=path)
    
# Create Legend
    ax.legend(loc='upper center', bbox_to_anchor=(0.85, .85),
              ncol=1, fancybox=True, shadow=True)    
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.xaxis.grid(color='gray', linestyle='dashed')

# Create plot
plt = matplotlib.pyplot.figure()
ax = axes()
    
# Save  plot
plt.set_facecolor('white')

for f in sys.argv[1:]:
    print "Adding %s" % f
    add_plot(f)

# plt.savefig('~/plot.png', bbox_inches=0)
show()
 


