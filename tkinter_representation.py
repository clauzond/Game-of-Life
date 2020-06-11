from tkinter import *
from tkinter.colorchooser import askcolor
import array_representation


class GameWindow():

    def __init__(self, canvasHeight, canvasWidth):

        self.canvasHeight = canvasHeight
        self.canvasWidth = canvasWidth

        self.GameOfLife = None

        self._createWindow()
        self._createWidgets()
        self._createBinds()

        self.gameWindow.mainloop()

    def hide(self):
        pass

    def _initGameOfLife(self):

        if self.GameOfLife is None:
            tempheight, tempwidth = self.heightScale.get(), self.widthScale.get()
            initialArray = None
            self.GameOfLife = array_representation.GameOfLife(
                height=tempheight, width=tempwidth, initial_array=initialArray)
        
            cube_nbr_height = self.canvasHeight//tempheight
            cube_nbr_width = self.canvasWidth//tempwidth
            
            self.cubeDim = min(cube_nbr_width, cube_nbr_height)

            canvasHeight = self.cubeDim*tempheight
            canvasWidth = self.cubeDim*tempwidth

            self.gameCanvas.config(height=canvasHeight)
            self.gameCanvas.config(width=canvasWidth)

            for x in range(0, tempheight):
                for y in range(0, tempwidth):
                    if self.GameOfLife.gameArray[x][y] == 1:
                        this_color = self.livingCellsColor
                    else:
                        this_color = self.deadCellsColor
                    self._drawOneCube(canvas=self.gameCanvas, cubeDim=self.cubeDim, line=x, column=y, color=this_color)
        else:
            this_shape = (self.heightScale.get(), self.widthScale.get())
            if this_shape != self.GameOfLife.shape:
                print("Erreur de dimensions")
            else:
                self.GameOfLife= array_representation.GameOfLife(height=this_shape[0],width=this_shape[1], initial_array=self.GameOfLife.gameArray)

                for x in range(0, this_shape[0]):
                    for y in range(0, this_shape[1]):
                        if self.GameOfLife.gameArray[x][y] == 1:
                            this_color = self.livingCellsColor
                        else:
                            this_color = self.deadCellsColor
                        self._drawOneCube(canvas=self.gameCanvas, cubeDim=self.cubeDim, line=x, column=y, color=this_color)


    def _drawOneCube(self, canvas, cubeDim, line, column, color):
        x0 = column*cubeDim
        y0 = line*cubeDim
        x1 = column*cubeDim + cubeDim
        y1 = line*cubeDim + cubeDim
        canvas.create_rectangle(x0,y0,x1,y1,fill=color)

    def _canvasShapeToArrayShape(self, canvasHeight, canvasWidth):
        pass

    def _drawCanvas(self, changedlist):
        """
        Draw the canvas according to a list of coordinates

        args:
            *changedlist -> list of coordinates that needs to be changed
        return:
            :None
        """
        for (x,y) in changedlist:
            if self.GameOfLife.gameArray[x][y] == 1:
                this_color = self.livingCellsColor
            else:
                this_color = self.deadCellsColor
            self._drawOneCube(canvas=self.gameCanvas, cubeDim=self.cubeDim, line=x, column=y, color=this_color)

    def _getMouseClickCoords(self, event):
        """
        Get mouse coordinates in line/column
        """

        if self.GameOfLife is not None:

            if (self.modeVar.get() == "editeur") and (self.startState != "nothing"):
                x = self.gameCanvas.canvasx(event.x)
                y = self.gameCanvas.canvasy(event.y)
                
                this_column = int(x // self.cubeDim)
                this_line = int(y // self.cubeDim)

                if self.GameOfLife.gameArray[this_line][this_column] == 1:
                    this_color = self.deadCellsColor
                    self.GameOfLife.gameArray[this_line][this_column] = 0  
                else:
                    this_color = self.livingCellsColor
                    self.GameOfLife.gameArray[this_line][this_column] = 1
                self._drawOneCube(canvas=self.gameCanvas, cubeDim=self.cubeDim, line=this_line, column=this_column, color=this_color)



    def _createWindow(self):
        self.gameWindow = Tk()
        self.gameWindow.title("Conway's Game of Life'")
        self.gameWindow.resizable(False, False)
        # self.gameWindow.iconbitmap("img/icone.ico")

        self.gameWindow.option_add('*Font', 'Constantia 12')
        #self.gameWindow.option_add('*Button.relief', 'flat')
        #self.gameWindow.option_add('*Button.overRelief', 'ridge')
        self.gameWindow.option_add('*justify', 'center')

        self.backgroundColor = "#292826"
        self.foregroundColor = "#F9D342"
        self.deadCellsColor = "#FFFFFF"
        self.livingCellsColor = "#000000"

        self.gameWindow.option_add('*background', self.backgroundColor)
        self.gameWindow.option_add('*foreground', self.foregroundColor)
        self.gameWindow.configure(bg=self.backgroundColor)

    def _createBinds(self):
        self.gameCanvas.bind("<Button-1>",self._getMouseClickCoords)

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
        self.gameCanvas = Canvas(
            self.windowFrame, height=self.canvasHeight, width=self.canvasWidth)
        self.gameCanvas.grid(row=0, column=0, rowspan=1, columnspan=30, pady=10)

        # BUTTONS
        """self.playState = "play"
        self.playButton = Button(
            self.windowFrame, text="Play", command=self._pressPlayButton)
        self.playButton.grid(row=1, column=1, rowspan=2)
        """

        self.startState = "nothing"
        self.startButton = Button(self.windowFrame, text="Start", command=self._pressStartButton)
        self.startButton.grid(row=1, column=1, rowspan=2)

        self.deadColorButton = Button(self.windowFrame,
                                      text="Dead",
                                      bg=self.deadCellsColor,
                                      command=self._changeColor1)
        self.deadColorButton.grid(row=1, column=0)
        self.livingColorButton = Button(self.windowFrame,
                                        text="Living",
                                        bg=self.livingCellsColor,
                                        command=self._changeColor2)
        self.livingColorButton.grid(row=2, column=0)

        # RADIO BUTTONS
        self.modeVar = StringVar(self.gameWindow, "observation")
        self.modeRadio1 = Radiobutton(self.windowFrame,
                                      text="Mode observation",
                                      variable=self.modeVar,
                                      value="observation",
                                      indicatoron=0)
        self.modeRadio1.grid(row=1, column=5)
        self.modeRadio2 = Radiobutton(self.windowFrame,
                                      text="Mode éditeur",
                                      variable=self.modeVar,
                                      value="editeur",
                                      indicatoron=0)
        self.modeRadio2.grid(row=2, column=5)

        # MUTABLE LABELS
        self.stepNumberLabel = Label(self.gameCanvas, text="Step: 0")
        self.stepNumberLabel.place(x=10, y=10)
        self.livingNumberLabel = Label(self.gameCanvas, text="Living : 0")
        self.livingNumberLabel.place(x=10, y=30)

        # SCALE & LABELS
        self.speedLabel = Label(self.windowFrame, text="Step per sec")
        self.speedLabel.grid(row=1, column=2)
        self.speedScale = Scale(self.windowFrame, from_=1,
                                to=10, orient="horizontal")
        self.speedScale.grid(row=2, column=2)

        self.heightLabel = Label(self.windowFrame, text="Height")
        self.heightLabel.grid(row=1, column=3)
        self.heightScale = Scale(
            self.windowFrame, from_=1, to=100, orient="horizontal")
        self.heightScale.grid(row=2, column=3)

        self.widthLabel = Label(self.windowFrame, text="Width")
        self.widthLabel.grid(row=1, column=4)
        self.widthScale = Scale(self.windowFrame, from_=1,
                                to=100, orient="horizontal")
        self.widthScale.grid(row=2, column=4)

    def _updateLabels(self):
        self.stepNumberLabel.config(text="")
        self.livingNumberLabel.config(text="")


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
            self.playButton.config(text="Pause")
        else:
            pass

            self.playState = "play"
            self.playButton.config(text="Play")

    def _pressStartButton(self):
        if self.modeVar.get() == "observation":
            if self.startState == "nothing":
                self.startButton.config(text="Next step")
                self.startState = "start"

                self.widthScale.config(state="disabled")
                self.heightScale.config(state="disabled")

                self.modeRadio1.config(state="disabled")
                self.modeRadio2.config(state="disabled")

                self._initGameOfLife()
            else:
                self._nextStepButton()
        elif self.modeVar.get() == "editeur":
            if self.startState == "nothing":
                self.startButton.config(text="Stop")
                self.startState = "start"

                self.widthScale.config(state="disabled")
                self.heightScale.config(state="disabled")
                self.modeRadio1.config(state="disabled")
                self.modeRadio2.config(state="disabled")

                self._initGameOfLife()
            else:
                self.startState = "nothing"
                self.startButton.config(text="Start")
                self.modeRadio1.config(state="normal")
                self.modeRadio2.config(state="normal")

    def _loopStep(self):
        pass

    def _nextStepButton(self):
        if self.GameOfLife is not None:
            this_list = self.GameOfLife.nextStep()
            self._drawCanvas(changedlist=this_list)
            self.stepNumberLabel.config(text = self.GameOfLife.totalSteps)
            self.livingNumberLabel.config(text = self.GameOfLife.livingCellsNumber)


    def _refreshColors(self):
        for x in range(0,self.GameOfLife.shape[0]):
            for y in range(0,self.GameOfLife.shape[1]):
                if self.GameOfLife.gameArray[x][y] == 1:
                    this_color = self.livingCellsColor
                else:
                    this_color = self.deadCellsColor
                self._drawOneCube(canvas=self.gameCanvas, cubeDim=self.cubeDim, line=x, column=y, color=this_color)

    def _changeColor1(self):
        try:
            rgb, colorStr = askcolor(
                title="Color", initialcolor=self.deadCellsColor, parent=self.gameWindow)
        except TclError:
            colorStr = None
        if colorStr is not None:
            self.deadCellsColor = str(colorStr)
            self.deadColorButton.config(bg=self.deadCellsColor)
            # self._drawCanvas()

            if self.GameOfLife is not None:
                self._refreshColors()


    def _changeColor2(self):
        try:
            rgb, colorStr = askcolor(
                title="Color", initialcolor=self.livingCellsColor, parent=self.gameWindow)
        except TclError:
            colorStr = None
        if colorStr is not None:
            self.livingCellsColor = str(colorStr)
            self.livingColorButton.config(bg=self.livingCellsColor)
            # self._drawCanvas()

            if self.GameOfLife is not None:
                self._refreshColors()


if __name__ == "__main__":
    w = GameWindow(canvasHeight=720, canvasWidth=1280)
