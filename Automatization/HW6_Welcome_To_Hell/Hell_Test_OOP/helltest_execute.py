
from hell_def import *

VisionThis = Visible()
Frame = Iframe()
Anketa = AnketaForm()
Text = TextForm()
Link = LinkCheck()


def Run():
    VisionThis.SomeElementsAreVisible()
    Frame.IFrameWorking()
    Anketa.AnketaChecking()
    Text.TextAssert()
    Link.LinkChecking()
    VisionThis.QuitBrowser()
    
Run()


