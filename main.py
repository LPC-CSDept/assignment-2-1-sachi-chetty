def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    male = float(input("males"))
    female = float(input("females"))
        
    total = male + female

    m_perc = (male / total) * 100.0
    f_perc = (female / total) * 100.0

    print (f"Total number of students: {int(total)}")
    print (f"The numbers of males and females: {int(male)} {int(female)}")
    print (f"The percentages of males and females: {m_perc:.2f}% {f_perc:.2f}%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
