#############################################################
### YOUTUBE TRANSCRIPT PARSER ###############################
### Kleinberg, Mozes, van der Vegt (ablphabetical order) ####
### https://github.com/ben-aaron188/youtube_ads_detection ###
#############################################################

#clear ws
rm(list = ls())

parent_dir = "/Users/bennettkleinberg/GitHub/youtube_ads_detection"
setwd(parent_dir)

#deps
source('./r_nlp/txt_df_from_dir.R')
source('./r_nlp/clean_transcript.R')

#input: read full directory of single files to df
transcripts = txt_df_from_dir(dirpath = './output_dir')

transcripts$text_clean = clean_transcript(transcripts$text)

View(transcripts)

# TODO:
#processing per file for vectorized structure

# split per word

# split proportionally

###END