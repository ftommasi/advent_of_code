
opcodes = [1,79,60,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0]
#opcodes = [1,9,10,3,2,3,11,0,99,30,40,50]
for i in range(0,len(opcodes),4):
    #print opcodes
    current_op = opcodes[i]
    operand_1 = opcodes[i+1]
    operand_2 = opcodes[i+2]
    destination = opcodes[i+3]
    #print "current op: {}".format(current_op)
    if current_op == 1 :
        #add
        temp_sum = opcodes[operand_1] + opcodes[operand_2]
        #print "op[{}] = op[{}]:{} + op[{}]:{} = {}".format(destination,operand_1,opcodes[operand_1],operand_2,opcodes[operand_2],temp_sum)
        opcodes[destination] = temp_sum
    elif current_op == 2:
        #mult
        temp_sum = opcodes[operand_1] * opcodes[operand_2]
        #print "op[{}] = op[{}]:{} * op[{}]:{} = {}".format(destination,operand_1,opcodes[operand_1],operand_2,opcodes[operand_2],temp_sum)
        opcodes[destination] = temp_sum
    elif current_op == 99:
        #stop
        #print "stopping..."
        #print ""
        break
    else:
        #encountered a bad opcode
        #print "error"
        break
    #print "--"
    #print ""

print opcodes
print opcodes[0]