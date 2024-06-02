class Deleted_Files():
    def __init__(self):
        pass

    #abre o arquivo, lê os dados e separa por dias retornando um array com todos os dias separados.
    def split_by_days(self, log_path = "Log_Limpeza_Dbordo.txt"):
        deleted_files = open(log_path,'r')
        separate_by_day = deleted_files.read().split("Hoje - ")

        deleted_files.close()

        return separate_by_day
    
    def break_lines(self,day):
        return day.split("\n")
    
    def split_line(self, line):
        return line.split("      ")
    
    def line(self, day):
        excluded_count = 0
        if len(day) > 4:
            data_name = day[0][:10]
            for line in range(4,len(day)):
                file = self.split_line(day[line])
                if len(file) > 0:
                    file_name = file[0]
                    if file_name:
                        excluded_count +=1
        else:
            data_name = "no data"
        return {data_name:excluded_count}
    
    def all_data(self):
        datas_to_return = {}
        for day in self.split_by_days():
            lines_of_day = self.break_lines(day)
            datas_to_return.update(self.line(lines_of_day))
        
        del datas_to_return["no data"]
        return datas_to_return