import clr
clr.AddReference("CrystalDecisions.CrystalReports.Engine")
from CrystalDecisions.CrystalReports.Engine import ReportDocument, Table
clr.AddReference("CrystalDecisions.Shared")
from CrystalDecisions.Shared import ExportFormatType, ExportOptions, ParameterField, ParameterFields, ParameterValues, ParameterDiscreteValue
import datetime

date_parameter = datetime.date.today() - datetime.timedelta(days=1)

report = ReportDocument()
report.Load('I:\\Mikes_Crystals\CDC_ofac_daily.rpt')
print('Locked and Loaded')

param1 = ParameterField()
param2 = ParameterField()
val1 = ParameterValues()
val2 = ParameterValues()
date1 = ParameterDiscreteValue()
date2 = ParameterDiscreteValue()


param1.ParameterFieldName = BeginDate
param2.ParameterFieldName = EndDate
date1.Value = date_parameter
date2.Value = date_parameter
val1.Add(date1)
val2.Add(date2)

report.SetParameterValue("1", val1)
report.SetParameterValue("2", val2)

print('Parameters set.')

report.SetDatabaseLogon('uwu', 'owo')
print('Credentials set.')
report.Refresh()
print('Report refreshed.')

exportOp = ExportOptions()
report.ExportToDisk(ExportFormatType.CharacterSeparatedValues, "report.csv")

print('File Exported?')