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
source('./r_nlp/wordcount.R')

#input: read full directory of single files to df
transcripts = txt_df_from_dir(dirpath = './output_dir')

transcripts$text_clean = clean_transcript(transcripts$text)

transcripts_clean = transcripts[, -1]

transcripts_clean$nwords = wordcount(transcripts_clean$text_clean)

sum(transcripts_clean$nwords)

write.table(transcripts_clean,
            file='clean_transcripts_10102017.txt',
            na = 'NA',
            sep = '\t',
            append=F,
            row.names = F,
            col.names = T
            )

save(transcripts_clean
     , file = 'clean_transcripts_10102017.RData')

# TODO:
#processing per file for vectorized structure

# split per word

# split proportionally

###END
