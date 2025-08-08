zipFile = matlab.internal.examples.downloadSupportFile("medical","MedicalVolumeNIfTIData.zip");
filepath = fileparts(zipFile);
unzip(zipFile,filepath)
dataFolder = fullfile(filepath,"MedicalVolumeNIfTIData");