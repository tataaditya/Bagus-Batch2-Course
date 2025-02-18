class databaseMahasiswa:
    # buat sebuah constructor untuk membaca file nama dan juga file nim. 
    # Jika tidak ada filenya, langsung buat
    def _init_(self, nama_file, nim_file):
        self.nama_file = nama_file
        self.nim_file = nim_file

        # bikin filenya kalo gaada
        file1 = open(self.nama_file, 'a')
        file2 = open(self.nim_file, 'a')
        file1.close()
        file2.close()


    # method untuk menambahkan data mahasiswa ke dalam
    # file txt. Tidak boleh ada data duplikat
    def add_student(self, nama, nim):
        with open(self.nim_file, 'r') as nim_file:
            nim_list = nim_file.readlines()

        for existing_nim in nim_list:
            if nim == existing_nim.strip():
                print(f"Error: Mahasiswa dengan NIM {nim} sudah ada!.")
                return 
            
        with open(self.nama_file, 'a') as nama_file, open(self.nim_file, 'a') as nim_file:
            nama_file.write(nama + "\n")
            nim_file.write(nim + "\n")

        print(f"Mahasiswa {nama} (NIM: {nim}) sudah ditambah!")

    # method untuk menampilkan semua data mahasiswa dalam format 
    # yang bagus banget dan ganteng kayak Bagusde baru habis potong rambut 
    def show_all_students(self):
        with open(self.nama_file, 'r') as nama_file:
            nama_list = nama_file.readlines()
        
        with open(self.nim_file, 'r') as nim_file:
            nim_list = nim_file.readlines()

        if len(nama_list) == 0:
            print('Tidak ada data dalam File!')
        else:
            print('List of Students:\n')
            print(f"{'No.':<5}{'Nama':<20}{'NIM':<15}")
            print("-" * 40)
            for i in range(len(nama_list)):
                print(f"{i + 1:<5}{nama_list[i].strip():<20}{nim_list[i].strip():<15}")

    #untuk delete by NIM: 
    # 1. Buka semua data, (kalo aku tak masukin ke dalam sebuah "list of dictionary")
    # 2. buat sebuah list new student kosong
    # 3. loop di setiap student. Kalo nim "tidak" sama dengan nimnya mahasiswa, 
    #    masukkan ke dalam list kosong (pakai .append())
    # 4. save dengan cara looping write untuk NIM dan juga nama
    # beres deh :D
    def delete_student(self, nim):
        students = self.student_to_dictionary()
        new_students = []

        for student in students:
            if student["NIM"] != nim:
                new_students.append(student)

        if len(new_students) < len(students):
            self._save_students(new_students)
            print("Student deleted successfully!")
        else:
            print("Student with the specified NIM not found.")


    def student_to_dictionary(self):
        with open(self.nama_file, 'r') as nama_file:
            nama_list = nama_file.readlines()
        
        with open(self.nim_file, 'r') as nim_file:
            nim_list = nim_file.readlines()

        students = []
        for i in range(len(nama_list)):
            student = {"Nama": nama_list[i].strip(), "NIM": nim_list[i].strip()}
            students.append(student)
        
        return students

    # Cara cari data dengan NIM
    # 1. Buka file, ambil data pakai readlines()
    # 2. Looping aja udah, di dalem loop pake if. 
    #    kalo ketemu datanya tinggal di print aja :D
    def search_student_by_nim(self, nim):
        with open(self.nama_file, 'r') as nama_file:
            nama_list = nama_file.readlines()
        
        with open(self.nim_file, 'r') as nim_file:
            nim_list = nim_file.readlines()

        for i in range(len(nim_list)):
            if nim_list[i].strip() == nim:
                print(f"Student Found: Nama: {nama_list[i].strip()}, NIM: {nim_list[i].strip()}")
                return {"Nama": nama_list[i].strip(), "NIM": nim_list[i].strip()}

        print("Student with the specified NIM not found.")
        return None


    def _save_students(self, students):
        with open(self.nama_file, 'w') as nama_file:
            for student in students:
                nama_file.write(student["Nama"] + "\n")

        with open(self.nim_file, 'w') as nim_file:
            for student in students:
                nim_file.write(student["NIM"] + "\n")

    # update by nim
    # 1. Buka semua data, (kalo aku tak masukin ke dalam sebuah "list of dictionary")
    # 2. looping di setiap datanya, jika ketemu nim sesuai, maka ganti nama dan juga nim
    # 3. kalo udah di update, maka save dengan cara looping write untuk NIM dan juga nama
    # beres deh :D
    def update_student(self, old_nim, new_nama=None, new_nim=None):

        students = self.student_to_dictionary()

        updated = False

        for student in students:
            if student["NIM"] == old_nim:
                if new_nama:
                    student["Nama"] = new_nama
                if new_nim:
                    student["NIM"] = new_nim
                updated = True
                break

        if updated:
            self._save_students(students)
            print("Student updated successfully!")
        else:
            print("Student with the specified NIM not found.")


# panggil lah mereka mbuahahahaha
db = databaseMahasiswa(r'Day19-20_Project3\nama.txt', r'Day19-20_Project3\nim.txt')
db.show_all_students()
db.add_student('Yogoi', '24151408247')
db.show_all_students()

# CRUD





# print(f'Nama : {nama.strip()}')