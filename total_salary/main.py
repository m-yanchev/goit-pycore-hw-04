def total_salary(path):
    
    try:
        with open( path, 'r' ) as file:
            total = 0
            lines = file.readlines()
        for line in lines:
            total += int( line.split(',')[1].strip() ) 
    
    except ValueError:
        print(f"Некоректний формат даних у файлі {path}.")
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")

    else:
        average = total / len(lines) if lines else 0
        return total, average
        
    return None, None
        

total, average = total_salary("total_salary/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")