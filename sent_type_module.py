from usr_func import get_wx_output_list

# Row 10:Sentence type
def get_row10(wxOutputList):
    sentence_type = []
    if "nahI" in wxOutputList or "nahIM" in wxOutputList:
        sentence_type.append('negative')
    else:
        if "?" in wxOutputList:
            sentence_type.append("interrogative")
        elif "|" in wxOutputList:
            sentence_type.append("affirmative")
        elif "." in wxOutputList:
            sentence_type.append("affirmative")
        elif "!" in wxOutputList:
            sentence_type.append("exclamatory")
    return sentence_type

if __name__ == "__main__":
    wxOutputList = get_wx_output_list() 
    row_10 = get_row10(wxOutputList)
    print(",".join(row_10))
