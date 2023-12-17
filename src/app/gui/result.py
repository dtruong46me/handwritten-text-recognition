from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class Result:
    def __init__(self, window, image_path="C:\\User\\DELL", predicted_text="hello") -> None:
        self.parent_path = Path(__file__).parent
        self.assets_path = self.parent_path / Path(f"../assets")

        self.window = window
        self.window.geometry("1200x800")
        self.window.configure(bg = "#FFFFFF")

        self.window.title("Handwritten Text Recognition")

        self.icon_path = PhotoImage(file=self.relative_to_assets("logo_h.png"))
        self.window.iconphoto(True, self.icon_path)

        
        self.canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 800,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0,y=0)
        
        self.logo_text = PhotoImage(
            file=self.relative_to_assets("logo_h.png"))
        self.logo_text_bg = self.canvas.create_image(
            165.0,
            58.0,
            image=self.logo_text
        )

        self.frame_left_img = PhotoImage(
            file=self.relative_to_assets("frame_l.png"))
        self.frame_left = self.canvas.create_image(
            352.0,
            433.0,
            image=self.frame_left_img
        )

        self.frame_right_img = PhotoImage(
            file=self.relative_to_assets("frame_r.png"))
        self.frame_right = self.canvas.create_image(
            912.0,
            433.0,
            image=self.frame_right_img
        )

        from PIL import Image, ImageTk

        min_width, min_height = 240, 112
        max_width, max_height = 540, 325

        image_pil = Image.open(image_path)
        width, height = image_pil.size
        
        if width > max_width and height < max_height:
            new_width = max_width
            new_height = int(height / width * new_width)
            image_pil = image_pil.resize((new_width, new_height), Image.LANCZOS)
        
        if height > max_height and width < max_width:
            new_height = max_height
            new_width = int(width / height * new_height)
            image_pil = image_pil.resize((new_width, new_height), Image.LANCZOS)

        if width > max_width and height > max_height:
            ratio = min(max_width/width, max_height/height)
            image_pil = image_pil.resize((int(width*ratio), int(height*ratio)), Image.LANCZOS)

        if width < min_width and height < min_height:
            ratio = min(min_width / width, min_height / height)
            image_pil = image_pil.resize((int(width*ratio), int(height*ratio)), Image.LANCZOS)

        self.selected_image = ImageTk.PhotoImage(image_pil)

        self.predict_image = self.canvas.create_image(
            353.0,
            427.0,
            image=self.selected_image
        )

        self.canvas.create_text(
            723.0,
            252.0,
            anchor="nw",
            text=predicted_text,
            fill="#363062",
            font=("Consolas Bold", 32 * -1),
            width=390
        )

        self.title_text = PhotoImage(
            file=self.relative_to_assets("title.png"))
        self.title_text_bg = self.canvas.create_image(
            599.0,
            153.0,
            image=self.title_text
        )

        self.continue_bg = PhotoImage(
            file=self.relative_to_assets("btn__continue.png"))
        self.continue_btn = Button(
            image=self.continue_bg,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_continue,
            relief="flat",
            background="#FFFFFF"
        )
        self.continue_btn.place(
            x=492.0,
            y=678.0,
            width=216.0,
            height=72.0
        )

    def handle_continue(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from main_screen import MainHTR
        self.main_gui = MainHTR(self.window)
        self.current_gui = self.main_gui
    
    def handle_link(self):
        return
    
    def handle_submit(self):
        return
        
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)

if __name__ == '__main__':
    window = Tk()
    htr_app = Result(window=window)
    window.resizable(False,False)
    window.mainloop()