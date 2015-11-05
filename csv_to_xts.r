#eurusd_csv <- system("sed '/T/!s/././18' EURUSD_1m_est.csv",intern=TRUE)
#toDate <- function(x) strptime(x, "%Y%m%d %H:%M:%OS")
system("/data/eurusd_awk.sh")
op <- options(digits.secs=3)
options(op)
#z <- read.zoo('EURUSD_2003-05-05_2015-10-24_est_1m.csv', header=TRUE, sep=',',
z <- read.zoo('eurusd_tmp.csv', header=TRUE, sep=',',
              format="%Y-%m-%d %H:%M:%OS", tz='EDT',
              index.column = 1,
              drop=FALSE,FUN=as.POSIXct)
eurusd <- as.xts(z)

op <- options(digits.secs=3)
options(op)
s <- system("sed -n '/2003-05-05 00:00:03.640/,/2003-05-06 00:00:00.000/p' EURUSD_2003-05-05_2015-10-24_est_1m.csv > tmp")

#s <- system(Wawk '$1 " " $2 >="2003-05-05 00:00:00.914" && $1 " " $2 <="2003-05-05 00:01:05.640"' <  EURUSD_2003-05-05_2015-10-24_est_1m.csv",intern=TRUE)

#s <- ("awk "substr($0,1,23)>='2003-05-05 00:00:00.914' && substr($0,1,23)<='2003-05-05 00:01:05.640'" <  EURUSD_2003-05-05_2015-10-24_est_1m.csv")

system("/data/eurusd_awk.sh")

system("/data/eurusd_awk.sh")
op <- options(digits.secs=3)
options(op)
z <- read.zoo('eurusd_tmp.csv',header=TRUE, sep=',',
            format="%Y-%m-%d %H:%M:%OS", tz='EDT',
            index.column = 1,
            drop=FALSE,FUN=as.POSIXct)

eurusd <- as.xts(z)

#EURUSD_2003-05-05_2015-10-24_est_1m.csv

eurusd <- as.xts(z)

eurusd3 <- read.csv.sql('EURUSD_2003-05-05_2015-10-24_est.csv',
           header=TRUE, sep=',',
           sql="select * from file where 
           Timestamp > '2003-05-06 00:00:01'and 
           Timestamp < '2003-07-06 00:00:01'")

eurusd3 <- read.csv.sql('EURUSD_09122015_est.csv',
                        header=TRUE, sep=',',
                        sql="select * from file where 
                        Timestamp > '20150803 00:00:01'and 
                        Timestamp < '20150806 00:00:01'")

eurusd3 <- as.xts(read.csv.sql('EURUSD_09122015_est.csv',
                               header=TRUE, sep=',',
                               sql="select * from file where 
                               Timestamp > '2015-08-06 00:00:01'and 
                               Timestamp < '2015-08-08 00:00:01'"),index.column=1)

as.xts( d, order.by=as.POSIXct(strptime(paste(d$Date, d$Time), '%m/%d/%y %H:%M'))) 

eurusd4 <- as.xts(eurusd3, 
           format="%Y%m%d %H:%M:%OS", tz='EDT',
           index.column = 1,
           drop=FALSE,FUN=as.POSIXct)

eurusd4 <- as.xts(eurusd3, 
                  format="%Y-%m-%d %H:%M:%OS", tz='EDT',
                  index.column = 1,
                  drop=FALSE,FUN=as.POSIXct)

data <- xts(data[,2:6], order.by = data$time, unique = FALSE, tzone = "")

eurusd <- as.xts(read.zoo('EURUSD_09122015_est.csv', header=TRUE, sep=',',
              format="%Y%m%d %H:%M:%OS", tz='EDT',
              index.column = 1,
              drop=FALSE,FUN=as.POSIXct))