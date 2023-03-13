data = read.csv('/Users/eb/Downloads/rr-interval-time-series-from-healthy-subjects-1.0.0/patient-info.csv')

file = '/Users/eb/Downloads/rr-interval-time-series-from-healthy-subjects-1.0.0/000.txt'

taco = read.delim(file, header = FALSE, sep = "\n")[1]
taco = taco$V1
x = 1:length(x)

length(x)
length(taco)

x11()
plot(x,taco, type="l", col="blue", lwd=0.01, xlab="Interval number", ylab="Interval length in ms", main="RR intervals")

x11()
plot(x[1:100],taco[1:100], type="l", col="blue", lwd=0.01, xlab="Interval number", ylab="Interval length in ms", main="RR intervals")

##  Time-domain features. 
# -Mean (mean of all RR intervals)
# -SDNN(standard deviation of all RR intervals)
# -RMSSD (root means square of differences between adjacent NN inter-
#           vals)
# -and SDSD (standard deviation of differences between adjacent NN intervals).

mean = mean(taco)
mean

sd = sd(taco)
sd

#per implementare rmssd e sdsd https://www.biopac.com/wp-content/uploads/app129.pdf
library('varian')
rmssd = rmssd(taco)
rmssd


## Frequency-domain features
library('lomb')
PSD = lsp(taco[1:100])

lsULF = sum(PSD$scanned >=0 & PSD$scanned<0.0033)
lsVLF = sum(PSD$scanned >=0.0033 & PSD$scanned<0.004)
lsLF = sum(PSD$scanned >=0.004 & PSD$scanned<0.015)
lsHF = sum(PSD$scanned >=0.015 & PSD$scanned<0.4)
lsLFHF = lsLF/lsHF

# lsULF = sum(PSD(f>=0 && f<0.0033))
# lsVLF = sum(PSD(f>=0.0033 and f<0.004))
# lSLF = sum(PSD(f>=0.004 and f<0.015))
# lsHF = sum(PSD(f>=0.015 and f<0.4))
# lsLFHF = lsLF/lsHF

## Nonlinear features. 
install.packages('pracma')
library('pracma')
sample_entropy(taco[1:4000])
