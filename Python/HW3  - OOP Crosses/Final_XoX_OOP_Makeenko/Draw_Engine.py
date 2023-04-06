
class Draw_Engine:
    FIELD_POSITION_TEXT_DICTIONARY = [" ", "X", "O"]
    def GetFieldPositionText(this, field, row, column):
        fieldPosition = field[row][column]
        return this.FIELD_POSITION_TEXT_DICTIONARY[fieldPosition]

    def ShowField(this, field):
        lineLength = 13
    
        for row in range(3):
            print("-" * lineLength)
            for column in range(3):
                print(f"| {this.GetFieldPositionText(field, row, column)} ", end='')
            print("|")
        print("-" * lineLength)

