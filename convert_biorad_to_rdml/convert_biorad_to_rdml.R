library(RDML)

###############################################
# function to convert BioRad text files to RDML so that it can run in LinRegPCR
###############################################
### INPUTS
## @param path: path to BioRad text/csv file. The file is in BioRAD's CSV format
 # The file is comma-delimited (e.g. subsequence entries are separated by comma)
 # The file has a row-header (e.g. the first row of cells describes the columns below it )
 # The first column of the file is blank
 # Each subsequent column represent an individual well across the cycles
 # The values given are raw fluorescence values from the instrument 
 # (e.g. not baseline subtracted, curve fitted or otherwise modified in any way)

## @param output_name: name of output file (not including extension name)

### OUTPUT
## a zipped XML format (RDML)

### EXAMPLES
# convert_rdml_to_biorad(
#  path = "biorad_FAM.txt", 
#  output_name = "biorad_FAM"
# )

###############################################
convert_rdml_to_biorad <- function(path, output_name) {
  
  # read csv file
  biorad_data <- read.csv(path)
  
  # remove the first column (The first column of the file is blank) 
  biorad_data <- biorad_data[,-1]
  
  # get the names of the individual wells
  biorad_wells <- colnames(biorad_data)[colnames(biorad_data)!= "Cycle"]
  
  # determine the number of wells (ie samples)
  number_of_samples <- length(biorad_wells)
  
  # mock up metadata needed for the RDML file format
  # each row is a well/sample
  description <- data.frame(
    fdata.name = biorad_wells, # must correspond to the column names in the biorad data
    exp.id = rep("exp1", number_of_samples), 
    run.id = rep("run1", number_of_samples), 
    react.id = 1:number_of_samples, 
    sample = paste0("sample", 1:number_of_samples),  
    sample.type = rep("unkn", number_of_samples), 
    target = rep("target1", number_of_samples), 
    target.dyeId = rep("dye_id", number_of_samples), 
    stringsAsFactors = FALSE
  )
  
  # create a new rdml class
  rdml_class <- RDML$new()
  
  # bind fluorescence values (from the biorad data) to the rdml class
  rdml_class$SetFData(biorad_data, description, fdata.type = "adp")
  
  # save as .RDML
  rdml_class$AsXML(paste0(output_name, ".RDML"))
  
}

