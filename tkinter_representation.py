from tkinter import *
from tkinter.colorchooser import askcolor
import array_representation as AR

class GameWindow():

    def __init__(self,canvasHeight,canvasWidth):

        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth

        self._createWindow()
        self._createWidgets()

        self.gameWindow.mainloop()


    def hide(self):
        pass
    def _drawCanvas(self,changedlist):
        """
        Draw the canvas according to a list of coordinates:
        """
        pass

    def _getMouseClickCoords(self,event):
        """
        Get mouse coordinates in line/column
        """
        pass

    def _createWindow(self):
        self.gameWindow = Tk()
        self.gameWindow.title("Conway's Game of Life'")
        self.gameWindow.resizable(False, False)
        #self.gameWindow.iconbitmap("img/icone.ico")

        self.gameWindow.option_add('*Font', 'Constantia 12')
        self.gameWindow.option_add('*Button.relief', 'flat')
        self.gameWindow.option_add('*Button.overRelief', 'ridge')
        self.gameWindow.option_add('*justify', 'left')

        self.backgroundColor = "#292826"
        self.foregroundColor = "#F9D342"
        self.deadCellsColor = "#FFFFFF"
        self.livingCellsColor = "#000000"


        self.gameWindow.option_add('*background', self.backgroundColor)
        self.gameWindow.option_add('*foreground', self.foregroundColor)
        self.gameWindow.configure(bg=self.backgroundColor)




    def _createWidgets(self):
        """
        Les widgets :
            FRAME :
                * Définir les dimensions de la fenêtre
            CANVAS :
                * Observation ou editeur
            BUTTONS :
                * Play/Pause
                * Change dead color (color 1)
                * Change alive color (color 2)
                * Change dims
            RADIO BUTTONS :
                * Mode observation
                * Mode editeur
            LABELS :
                * Step number
                * Number of living cells
            SCALE :
                * Steps per second
            ENTRIES :
                * Change dims

        """

        # FRAME
        self.windowFrame = Frame(self.gameWindow)
        self.windowFrame.pack()

        # CANVAS
        self.gameCanvas = Canvas(self.windowFrame,height=self.canvasHeight,width=self.canvasWidth)
        self.gameCanvas.grid(row=1,column=0,rowspan=3,columnspan=3)

        # BUTTONS
        self.playState = "play"
        self.playButton = Button(self.windowFrame,text="PLAY",command=self._pressPlayButton)
        self.playButton.grid(row=3+2,column=1)
        self.deadColorButton = Button(self.windowFrame,
                                        text="DEAD",
                                        bg=self.deadCellsColor,
                                        command=self._changeColor1)
        self.deadColorButton.grid(row=0,column=1)
        self.livingColorButton = Button(self.windowFrame,
                                            text="LIVING",
                                            bg=self.livingCellsColor,
                                            command=self._changeColor2)
        self.livingColorButton.grid(row=0,column=2)

        # RADIO BUTTONS
        self.modeVar = StringVar(self.gameWindow,"observation")
        self.modeRadio1 = Radiobutton(self.windowFrame,
                                    text="Mode observation",
                                    variable=self.modeVar,
                                    value="observation",
                                    indicatoron=0,
                                    command=self._changeRadio)
        self.modeRadio1.grid(row=1,column=3+1)
        self.modeRadio2 = Radiobutton(self.windowFrame,
                                        text="Mode editeur",
                                        variable=self.modeVar,
                                        value="editeur",
                                        indicatoron=0,
                                        command=self._changeRadio)
        self.modeRadio2.grid(row=2,column=3+1)

        # LABELS
        self.stepNumberLabel = Label(self.gameCanvas,text="0")
        self.stepNumberLabel.place(x=10,y=10)
        self.livingNumberLabel = Label(self.gameCanvas,text="0")
        self.livingNumberLabel.place(x=10,y=30)

        # SCALE
        self.scale = Scale(self.windowFrame, from_=1, to=10, orient="horizontal")
        self.scale.grid(row=3+2,column=2)




    def _updateLabels(self):
        self.stepNumberLabel.config(text="")
        self.livingNumberLabel.config(text="")

    def _changeRadio(self,*args):
        this_mode = self.modeVar.get()

        if this_mode == "observation":
            self.modeRadio1.select()
        elif this_mode == "editeur":
            self.modeRadio2.select()

    def _getHeight(self):
        pass

    def _getWidth(self):
        pass

    def _getSpeed(self):
        """
        Get the steps per second of the cursor widget
        """
        pass

    def _pressPlayButton(self):
        if self.playState == "play":
            pass

            self.playState = "pause"
            self.playButton.config(text="PAUSE")
        else:
            pass

            self.playState = "play"
            self.playButton.config(text="PLAY")

    def _loopStep(self):
        pass

    def _nextStepButton(self):
        pass

    def _changeColor1(self):
        try:
            rgb, colorStr = askcolor(title="Color",initialcolor=self.deadCellsColor,parent=self.gameWindow)
        except TclError:
            colorStr = None
        if colorStr is not None:
            self.deadCellsColor = str(colorStr)
            self.deadColorButton.config(bg=self.deadCellsColor)
            #self._drawCanvas()

    def _changeColor2(self):
        try:
            rgb, colorStr = askcolor(title="Color",initialcolor=self.livingCellsColor,parent=self.gameWindow)
        except TclError:
            colorStr = None
        if colorStr is not None:
            self.livingCellsColor = str(colorStr)
            self.livingColorButton.config(bg=self.livingCellsColor)
            #self._drawCanvas()


if __name__=="__main__":
    w = GameWindow(canvasHeight=500,canvasWidth=500)