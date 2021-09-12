#argument solution is optional, when true, the function displays the result.

def arithmetic_arranger(problems, solution=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  first_line = second_line = third_line = fourth_line = result_line = ""

  for p in problems:
    parts = p.split(" ")
    op1 = parts[0]
    symb = parts[1]
    op2 = parts[2] 

    if not symb in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."
    elif not op1.isdigit() or not op2.isdigit():
      return "Error: Numbers must only contain digits."
    elif len(op1) > 4 or len(op2) > 4:
      return "Error: Numbers cannot be more than four digits."

    first_line += op1.rjust(5)+'\t'
    second_line += symb.ljust(5)+'\t'
    third_line += op2.rjust(5)+'\t'
    result_line += "-----"+'\t'
    if solution:
      if symb == '+':
        result = int(op1) + int(op2)
      else:
        result = int(op1) - int(op2)
      fourth_line += str(result).rjust(5)+'\t'
    else:
      fourth_line = ""
    #end if solution 
    
  #end for problems

  arranged_problems = first_line+'\n'+second_line+'\n'+third_line+'\n'+result_line+'\n'+fourth_line

  return arranged_problems
