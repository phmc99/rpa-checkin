import pyautogui
import time
import schedule
import values

def checkin():
    pyautogui.PAUSE = 0.5

    # Desbloquear a tela do pc
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.moveTo(670, 476)
    pyautogui.click()
    pyautogui.write("21051470")
    pyautogui.press("enter")
    time.sleep(5)

    # Abrir o slack
    pyautogui.press("winleft")
    time.sleep(2)
    pyautogui.moveTo(648, 66)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.write("Slack")
    pyautogui.press("enter")
    time.sleep(2)

    # Fechar alguma thread se estiver aberta
    pyautogui.moveTo(1351, 153)
    pyautogui.click()

    # Abrir grupo "mar-21-gustavo"
    time.sleep(2)
    pyautogui.moveTo(657,107)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.write("mar-21-gustavo")
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(2)

    # Abrir a thread
    pyautogui.moveTo(1234,495)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.write(f"1- {values.ATIVIDADE}")
    pyautogui.hotkey("shift", "enter")
    pyautogui.write(f"2- Sem problemas\n")

    pyautogui.alert("Check-in!")

    print("Fim do script")

   
def main():
    schedule.every().day.at(f"{values.HORA}").do(checkin)

    while True:
        schedule.run_pending()
        time.sleep(1)
          

if __name__ == "__main__":
    main()
