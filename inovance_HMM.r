library("depmixS4") #the HMM library we’ll use 
library("quantmod") #a great library for technical analysis and working with time series 

Date<-as.character(EURUSD1d[,1])
DateTS<- as.POSIXlt(Date, format="%Y.%m.%d %H:%M:%S") #create date and time objects
TSData<-data.frame(EURUSD1d[,2:5],row.names=DateTS)
TSData<-as.xts(TSData) #build our time series data set

ATRindicator<-ATR(TSData[,2:4],n=14) #calculate the indicator
ATR<-ATRindicator[,2] #grab just the ATR

LogReturns <- log(EURUSD$Close) - log(EURUSD$Open) #calculate the logarithmic returns 

ModelData<-data.frame(LogReturns,ATR) #create the data frame for our HMM model

ModelData<-ModelData[-c(1:14),] #remove the data where the indicators are being calculated

colnames(ModelData)<-c("LogReturns","ATR") #name our columns

set.seed(1)
HMM<-depmix(list(LogReturns~1,ATR~1),data=ModelData,nstates=3,family=list(gaussian(),gaussian())) 
   #We’re setting the LogReturns and ATR as our response variables, using the data frame we just built, want to set 3 different regimes,
   #and setting the response distributions to be gaussian.

HMMfit<-fit(HMM, verbose = FALSE) #fit our model to the data set

print(HMMfit) #we can compare the log Likelihood as well as the 
              #AIC and BIC values to help choose our model

summary(HMMfit)

HMMpost<-posterior(HMMfit) #find the posterior odds for each state over our data set

head(HMMpost) #we can see that we now have the probability for each 
           #state for everyday as well as the highest probability class.


