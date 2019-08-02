import clr
clr.AddReference("CrystalDecisions.CrystalReports.Engine")
from CrystalDecisions.CrystalReports.Engine import ReportDocument, Table
clr.AddReference("CrystalDecisions.Shared")
from CrystalDecisions.Shared import ExportFormatType, ExportOptions


report = ReportDocument()
report.Load('bal_gt_250g_aggregate.rpt')
print('Locked and Loaded')

report.SetDatabaseLogon('xp2', 'xp2user')
print('Credentials set.')
report.Refresh()
print('Report refreshed.')

exportOp = ExportOptions()
report.ExportToDisk(ExportFormatType.RichText, "report.rtf")

print('File Exported?')