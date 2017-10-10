###############################################################################
### Returns wordcount of string
### credit to: https://gist.github.com/atbradley/5902375
###############################################################################

wordcount <- function(str) {
  sapply(gregexpr("\\b\\W+\\b", str, perl=TRUE), function(x) sum(x>0) ) + 1
}

#usage example:

#df$nwords = wordcount(df$target_string)

###
