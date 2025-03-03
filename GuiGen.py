import tkinter
import customtkinter
import datetime
import time
import os
import shutil
import pandas as pd
# from Scripts import FileGen
from tkinter import filedialog
from random import randint, choice
import pandas as pd
import glob


VERSION_Consolidated_Gen = "0.1.0"
ManafestGen_VERSION = "ManafestGen 0.1.0"
FileGen_VERSION = "FileGen 0.1.0"

selected_file_directory = open("Folderinfo.txt", "r")


# Random Face Generator
if randint(0,1):
    Random_Face = ":)"
elif randint(0,1):
    Random_Face = ":D"
elif randint(0,1):
    Random_Face = "(o_o)"
else:
    Random_Face = "(O-O)"
#else:
#    Random_Face = "\(o_o)/"

# Random Title Generator
if randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Consolidated Manafest Generator'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Conslidate Gen more like Gen Conslidated! {Random_Face}'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} This is a totally normal title. Nothing to see here! {Random_Face}'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} These are not the droids you are looking for! - Obi Bin Canoli'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Have you ever heard the tradjety of Darth Pagerism the unwise - Definitly not the sith lord'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Luke. I am not your father. I have no idea who you are - Dark Vader'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} The force is a path to many powers some people call. Wait thats not the line... {Random_Face}'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} The Cake is a lie'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Theres a snake in my boot'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} {Random_Face}'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Parkor! -the great Scott Micheal'
elif randint(0,1):
    Random_Title = f'{VERSION_Consolidated_Gen} Who you gonna call... 1-800-Got-Junk! {Random_Face}'
else:
    Random_Title = f'{VERSION_Consolidated_Gen} Dude you litterally got the rarest title. You won a gold star and a waffle :D'

# Manafest Gen
def Gen_Consolidated_CSV_Manafest():
    print("Running", "|",FileGen_VERSION, "|",ManafestGen_VERSION)

    # Datetime func
    just_time = datetime.datetime.now()
    formated_time = just_time.strftime("%H:%M:%S")
    formated_date = just_time.strftime("%m-%d-%y")

    # print func
    file_added_print = print("File added"" at "f'{formated_time}')
    file_delete_print = print("File removed"" at "f'{formated_time}')
    file_attempted_delete_print = print("File attempted delete"" at "f'{formated_time}')
    file_removed_temp_file_print = print("File TemporaryGen.csv deleted"" at "f'{formated_time}')
    file_attempt_removed_temp_file_print = print("File TemporaryGen.csv failed attempted delete"" at "f'{formated_time}')

    # Basic Vocabulary
    Temp_Doc = 'InputDocs/TemporaryGen.CSV'

    # Read Folderinfo to obtain directory for selected folder


    # Gets users home directory for filepaths
    home_dir = os.path.expanduser("~")

    # Consolidate CSV Documents
    # Path to input documents
    path = f'{selected_file_directory.read()}'
    extension = '.csv'

    # Func delete temporary file
    def delete_temp_file():
        try:
            os.remove(Temp_Doc)
            file_removed_temp_file_print
        except FileNotFoundError:
            file_attempt_removed_temp_file_print

    # Combine CSV Files
    # Delete old temp file if it exsists
    delete_temp_file()

    # Consolidate CSV files
    input_files = [file for file in os.listdir(path) if file.endswith(extension)]

    # Take consolidated csv files add together then, output Temp_Doc
        # Temp_Doc is the temporary CSV document for pandas to access
    dfs = []
    for file in input_files:
        df = pd.read_csv(os.path.join(path, file))
        dfs.append(df)
        file_added_print

    Temp_Gen_File = pd.concat(dfs, ignore_index=True)

    Temp_Gen_File.to_csv(Temp_Doc, index=False)

    # Input Consolidated CSV Document
    df = pd.read_csv('InputDocs/TemporaryGen.CSV')

    # Drop unwanded columns
    df = df.drop(columns = "group")
    df = df.drop(columns = "case")
    df = df.drop(columns = "barcode")
    df = df.drop(columns = "manSerial")
    df = df.drop(columns = "coo")
    # df = df.drop(columns = "value")
    # df = df.drop(columns = "weight")

    # Consolidateds and adds the weight and qty together
    # df1 = consolidated and sorted document
    df1 = df.groupby(by='product').agg({'weight': 'sum',
                                        'qty': 'sum'}).reset_index()

    # Sorts Output CSV by A to Z
    df1. sort_values ("product", ascending = True)

    # Re-order columnbs output
    df1 = df1[['qty', 'product', 'weight']]

    #Export Finished CSV File.
    df1.to_csv('InputDocs/ConsolidatedGen_Temp_Output.CSV', index=False)

    delete_temp_file()

    #You know what this does
    print("Done :)")

# GUI Generator
if __name__ == "__main__":
    # Gets users home directory for filepaths
    home_dir = os.path.expanduser("~")

    # Datetime func
    just_time = datetime.datetime.now()
    formated_time = just_time.strftime("%H:%M:%S")
    formated_date = just_time.strftime("%m-%d-%y")

    # Func Def
        # Rename generated file
    def rename_gen_output():
        try:
            os.rename('InputDocs/ConsolidatedGen_Temp_Output.CSV', 
                    f'InputDocs/{entry_output_filename.get()} {formated_date}.CSV')
            print(f'Renamed file to InputDocs/{entry_output_filename.get()}')
        except FileNotFoundError:
            print(f"Error: File not found InputDocs/ConsolidatedGen_Temp_Output.CSV.")
        except FileExistsError:
            print(f'Error: File {entry_output_filename.get()} already exists.')
        except Exception as e:
            print(f"An error occurred:")

    def move_renamed_output():
        try:
            os.rename(f'InputDocs/{entry_output_filename.get()} {formated_date}.CSV', 
                    f'{home_dir}/downloads/{entry_output_filename.get()} {formated_date}.CSV')
            print(f'Renamed file to InputDocs/{entry_output_filename.get()}')
        except FileNotFoundError:
            print(f"Error: File not found InputDocs/ConsolidatedGen_Temp_Output.CSV.")
        except FileExistsError:
            print(f'Error: File {entry_output_filename.get()} already exists.')
        except Exception as e:
            print(f"An error occurred:")

    # Set theme
    GuiApp = customtkinter.CTk()
    GuiApp.geometry("800x130")
    customtkinter.set_default_color_theme("green")
    customtkinter.set_appearance_mode("system")
    GuiApp.title(Random_Title)
    


    # select file for consoliation system
    def select_file_for_consolidation():
        selected_file_path = filedialog.askdirectory(initialdir=f'{home_dir}/downloads')
                                            
        if selected_file_path:
                print("Selected file:", selected_file_path)
                textdoc = open('Folderinfo.txt', 'w')
                textdoc.write(f'{selected_file_path}')
                textdoc.close
                
                # Do something with the file path, e.g., open and read the file


    # Button to select folder
    Select_file_button = customtkinter.CTkButton(GuiApp, text="Select Folder to Consolidate From", command=select_file_for_consolidation)
    Select_file_button.pack(pady=2)

    # Custom file name entry box
    entry_output_filename = customtkinter.CTkEntry(GuiApp, placeholder_text="Show Name Here")
    entry_output_filename.configure(state="normal", width=300, height=20)
    entry_output_filename.pack(pady=5)

    # Activate file gen / rename file / move file
    def Activate_Con_Gen():
        Gen_Consolidated_CSV_Manafest()
        rename_gen_output()
        print(f'{entry_output_filename.get()}')
        move_renamed_output()

    Consolidated_Gen_Button = customtkinter.CTkButton(GuiApp, text="Consolidate and Generate File", command=Activate_Con_Gen)
    Consolidated_Gen_Button.pack(pady=2)

    # Quit button
    def quit_command():
        quit()

    quit_button = customtkinter.CTkButton(GuiApp, text="Quit", command=quit_command)
    quit_button.pack(pady=2)




    # Run the Gui
    GuiApp.mainloop()