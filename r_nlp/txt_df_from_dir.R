###############################################################################
### Creates a dataframe with raw texts from directory
### Usable in spacy_ner_r pipeline
###############################################################################

txt_df_from_dir = function(dirpath){
  currentwd = getwd()
  setwd(dirpath)
  file_list = list.files()
  data = do.call("rbind"
                 , lapply(file_list
                          , FUN=function(files) {
                            print(files)
                            print(nchar(readChar(files
                                                 , file.info(files)$size)))
                            paste(files
                                  , readChar(files
                                            , file.info(files)$size)
                                  , sep="!!!!!!!!!")
                          }
                 )
  )

  id = 1:nrow(data)
  data = cbind(data, id)

  data = as.data.frame(data)
  names(data) = c('text', 'id')

  data$Filename = as.factor(str_extract(data$text, '^[^!!!!!!!!!]*'))
  data$text = sub('.*\\!!!!!!!!!(.*)','\\1', data$text)

  data = data[,-2]

  setwd(currentwd)

  return(data)
}

#usage example:

#new_data = txt_df_from_dir(dirpath = '/Users/bennettkleinberg/Documents/Research/CBDMI_Schiphol/michigan/comparative_paper/data/final/trials/truthful')

#View(new_data)
