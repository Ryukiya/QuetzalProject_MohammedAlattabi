from Bestelling import Bestelling
from BinaireZoekboom import BST, createTreeItem
from CirculaireDubbelGelinkteKetting import CirculaireGelinkteChain
from Gebruiker import Gebruiker
from MyQueue import MyQueue
from MyStack import MyStack
from Reservatie import ReservatieSysteem
from Werknemer import Werknemer

def Scenario1():
    r=ReservatieSysteem()
    r.Tijd=0
    WerknemerA=Werknemer('A','',10)

    r.Werknemers=CirculaireGelinkteChain()
    r.Werknemers.insert(0,WerknemerA)
    r.Order=MyStack()
    r.Order.push(WerknemerA)

    WerknemerB=Werknemer('B','',3)

    r.Werknemers.insert(1,WerknemerB)
    r.Order.push(WerknemerB)

    Bestelling1=Bestelling(0,5,False)




    r.Bestellingen=MyQueue(9)
    r.Bestellingen.enqueue(Bestelling1)
    Bestelling2=Bestelling(1,8,False)
    r.Bestellingen.enqueue(Bestelling2)

    r.SetTime(2)

    HuidigeBestelling1=r.Bestellingen.dequeue()[0]
    HuidigeWerknemer1=r.Order.pop()[0]
    HuidigeWerknemer1.assign(HuidigeBestelling1)

    HuidigeBestelling2=r.Bestellingen.dequeue()[0]
    HuidigeWerknemer2=r.Order.pop()[0]
    HuidigeWerknemer2.assign(HuidigeBestelling2)
    r.Increment()

    HuidigeWerknemer1.SubstractMax()
    HuidigeWerknemer1.Done()
    r.Order.push(HuidigeWerknemer1)

    r.boom=BST()
    r.boom.searchTreeInsert(createTreeItem(0,Bestelling1))
    r.Increment()

    HuidigeWerknemer2.SubstractMax()
    HuidigeWerknemer2.Done()
    r.Order.push(HuidigeWerknemer2)

    r.boom.searchTreeInsert(createTreeItem(1,Bestelling2))

def Scenario2():
    r=ReservatieSysteem()
    r.Tijd = 0
    GebruikerA=Gebruiker(0,'Els','','')
    GebruikerB=Gebruiker(1,'Tom','','')


    r.Gebruikers = CirculaireGelinkteChain()
    r.Gebruikers.insert(0, GebruikerA)
    r.Gebruikers.insert(1, GebruikerB)

    WerknemerA=Werknemer('A', '', 10)
    r.Werknemers=CirculaireGelinkteChain()
    r.Werknemers.insert(0, WerknemerA)

    r.Order = MyStack()
    r.Order.push(WerknemerA)


    WerknemerB=Werknemer('B', '', 3)
    r.Werknemers.insert(1, WerknemerB)

    r.Order.push(WerknemerB)

    Bestelling1=Bestelling(0, 0, False)

    r.Bestellingen=MyQueue(9)
    r.Bestellingen.enqueue(Bestelling1)

    Bestelling2=Bestelling(1, 1, False)
    Bestelling2.voegChocoladeToe(2)
    Bestelling2.voegHoningToe(1)

    r.Bestellingen.enqueue(Bestelling2)

    r.SetTime(1)

    HuidigeBestelling1=r.Bestellingen.dequeue()[0]

    HuidigeWerknemer1=r.Order.pop()[0]

    HuidigeWerknemer1.assign(HuidigeBestelling1)

    HuidigeBestelling2=r.Bestellingen.dequeue()[0]

    HuidigeWerknemer2=r.Order.pop()[0]

    HuidigeWerknemer2.assign(HuidigeBestelling2)

    r.Increment()

    HuidigeWerknemer1.SubstractMax()
    HuidigeWerknemer2.SubstractMax()

    r.boom=BST()
    if HuidigeWerknemer1.Done(): #Reference CHATGPT Layout
        r.Order.push(HuidigeWerknemer1)
        r.boom.searchTreeInsert(createTreeItem(0, Bestelling1))

    r.Increment()

    HuidigeWerknemer1.SubstractMax()
    HuidigeWerknemer2.SubstractMax()

    if HuidigeWerknemer2.Done(): #ReferenceChatGPT Layout
        r.Order.push(HuidigeWerknemer2)
        r.boom.searchTreeInsert(createTreeItem(1, Bestelling2))



def main():
    Scenario1()
    Scenario2()



if __name__ == "__main__":
    main()