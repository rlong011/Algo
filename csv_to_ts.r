#eurusd_csv <- system("sed '/T/!s/././18' EURUSD_1m_est.csv",intern=TRUE)
toDate <- function(x) strptime(x, "%Y%m%d %H:%M:%OS")
op <- options(digits.secs=3)
options(op)
z <- read.table('EURUSD_1m_est_up2.csv', header=TRUE, sep=',')
              #format="%Y%m%d %H:%M:%OS",
              #index.column = 1,
              #drop=FALSE,FUN=as.POSIXct)
eurusd2 <- as.ts(z)

z[,1] <- strptime(z[,1],"%Y%m%d %H:%M:%OS", tz='EDT')