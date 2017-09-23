###############################################################################
### Cleans data from scraped youtube transcripts
###############################################################################


#!!! needs dependency "txt_df_from_dir"

clean_transcript = function(input_column){
  #remove tags
  no_tags = gsub("<.*?>", "", input_column)

  #remove arrows -->
  no_arrows = gsub("-->", "", no_tags)

  #remove text in brackets
  no_brackets = gsub("\\[.*?\\]", "", no_arrows)

  #remove newlines
  no_newline = gsub("\\n", "", no_brackets)

  #remove time indicator
  no_time = gsub("[[:digit:]]{2,}:[[:digit:]]{2}:[[:digit:]]{2},[[:digit:]]{3}", "", no_newline)

  #remove dashes
  no_dash = gsub("-", "", no_time)


  #remove trailing and leading whitespace
  no_ws = trimws(no_dash)

  #refine multiple whitespaces to one
  fine_ws = gsub(" {2,}", " ", no_ws)

  return(fine_ws)

}

#usage example:

#transcripts = txt_df_from_dir(dirpath = './output_dir')

# --->
#transcripts$clean = clean_transcript(transcripts$text)

#View(transcripts)

