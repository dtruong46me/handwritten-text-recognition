from pathlib import Path
import os
import sys

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

class MainHTR:
    def __init__(self, window) -> None:
        self.parent_path = Path(__file__).parent
        self.assets_path = self.parent_path / Path(f"../assets")
        self.test_path = self.parent_path.parent / Path(f"../test")

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

        self.shorten_path = ""

        self.canvas.place(x = 0, y = 0)
        
        self.logo_text = PhotoImage(
            file=self.relative_to_assets("logo_h.png"))
        self.logo_text_bg = self.canvas.create_image(
            165.0,
            58.0,
            image=self.logo_text
        )

        self.canvas.place(x = 0, y = 0)
        self.frame_bg = PhotoImage(
            file=self.relative_to_assets("frame.png"))
        self.frame = self.canvas.create_image(
            600.0,
            433.0,
            image=self.frame_bg
        )

        self.img_image = PhotoImage(
            file=self.relative_to_assets("btn__image.png"))
        self.image_btn = Button(
            image=self.img_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_upload,
            relief="flat"
        )
        self.image_btn.place(
            x=494.0,
            y=359.0,
            width=213.0,
            height=136.0
        )

        self.img_upload = PhotoImage(
            file=self.relative_to_assets("btn__upload.png"))
        self.upload_btn = Button(
            image=self.img_upload,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_upload,
            relief="flat"
        )
        self.upload_btn.place(
            x=500.0,
            y=512.0,
            width=200.0,
            height=60.0
        )

        self.img_link = PhotoImage(
            file=self.relative_to_assets("btn__link.png"))
        self.link_btn = Button(
            image=self.img_link,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_link,
            relief="flat"
        )
        self.link_btn.place(
            x=707.0,
            y=512.0,
            width=60.0,
            height=60.0
        )

        self.img_submit = PhotoImage(
            file=self.relative_to_assets("btn__submit.png"))
        self.submit_btn = Button(
            image=self.img_submit,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_submit,
            relief="flat"
        )
        self.submit_btn.place(
            x=492.0,
            y=678.0,
            width=216.0,
            height=72.0
        )

        self.upload_text = PhotoImage(
            file=self.relative_to_assets("upload_y_img.png"))
        self.upload_text_bg = self.canvas.create_image(
            600.0,
            317.0,
            image=self.upload_text
        )

        self.title_text = PhotoImage(
            file=self.relative_to_assets("title.png"))
        self.title_text_bg = self.canvas.create_image(
            599.0,
            153.0,
            image=self.title_text
        )

    def handle_upload(self) -> str:
        self.file_path = filedialog.askopenfilename(
            initialdir="/",
            title="Choose image",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.heic"), ("All files", "*.*"))
        )

        if self.file_path:
            self.absolute_path = Path(self.file_path).resolve()
            
            self.upload_btn.place_forget()
            self.image_btn.place_forget()
            self.link_btn.place_forget()

            ## Remove self.upload_text_bg
            if self.upload_text_bg:
                self.canvas.delete(self.upload_text_bg)

            self.delete_img = PhotoImage(
                file=self.relative_to_assets("btn__delete.png"))
            
            self.delete_btn = Button(
                image=self.delete_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.handle_delete,
                relief="flat",
                background="#FFFFFF"
            )

            self.delete_btn.place(
                x=573.0,
                y=567.0,
                width=54.0,
                height=54.0
            )

            from PIL import Image, ImageTk

            min_width, min_height = 281, 123
            max_width, max_height = 740, 258

            image_pil = Image.open(self.absolute_path)
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

            self.sample_bg = ImageTk.PhotoImage(image_pil)


            # self.sample_bg = PhotoImage(
            #     file=self.relative_to_assets("c04-110-00.jpg"))
            self.sample_img = self.canvas.create_image(
                600.0,
                380.0,
                image=self.sample_bg
            )

            if len(str(self.absolute_path)) > 70:
                self.shorten_path = str(self.absolute_path)[:20] + "..." + str(self.absolute_path)[-50:]

            else:
                self.shorten_path = str(self.absolute_path)
                padding = int(73 - len(self.shorten_path)) // 2
                self.shorten_path = str(" " * padding) + self.shorten_path

            self.imagepath_text = self.canvas.create_text(
                269.0,
                532.0,
                anchor="nw",
                text=self.shorten_path,
                fill="#435585",
                font=("Consolas", 16 * -1),
                justify="center"
            )
    
    def handle_link(self):
        return
    
    def handle_submit(self):
        PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        PARENT_PATH = os.path.join(PARENT_PATH, "..")
        sys.path.insert(0, PARENT_PATH)
        from utils.inference import predict_image

        # ## ============PREDICT IMAGE TEXT ============
        generated_text = "Become success with a dise and hey presio! You're a star ... Rally sings as Uth"
        generated_text = predict_image(imagepath=self.absolute_path)

        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from result import Result
        self.result_gui = Result(self.window,image_path=self.absolute_path, predicted_text= generated_text)
        self.current_gui = self.result_gui
    
    def handle_delete(self):
        self.current_gui = None
        for widget in self.window.winfo_children():
            widget.destroy()

        from main_screen import MainHTR
        self.main_gui = MainHTR(self.window)
        self.current_gui = self.main_gui
        
    def relative_to_assets(self, path: str) -> Path:
        return self.assets_path / Path(path)


if __name__ == '__main__':
    window = Tk()
    htr_app = MainHTR(window=window)
    window.resizable(False,False)
    window.mainloop()