def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = 60
    female = 40
        
    total = male + female

    m_perc = male / total * 100
    f_perc = female / total * 100

    print (f"Total number of students: {total}")
    print (f"The numbers of males and females: {male} {female}")
    print (f"The percentages of males and females: {m_perc}% {f_perc}%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
