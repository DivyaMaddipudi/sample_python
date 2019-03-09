DirectoryInfo di = new DirectoryInfo(ProcessingDirectory)
FileInfo[] TXTFiles = di.GetFiles("*.xml")
if (TXTFiles.Length == 0)
{
    log.Info("no files present")
}
foreach (var fi in TXTFiles)
    log.Info(fi.Exists)