<<<<<<< HEAD
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_structures.stack import Stack

def run_test():
    print("--- TESTING STACK (POINTER BASED) ---")
    st = Stack()
    
    # KOREKSI: Gunakan method is_empty(), jangan akses st.items
    print(f"Uji Kosong Awal: {st.is_empty()}") 
    
    st.push("Lokasi-Petani-01")
    st.push("Lokasi-Gudang-01")
    st.push("Lokasi-Pasar-01")
    print(f"Uji Kosong Setelah Push: {st.is_empty()}")
    
    print(f"Pop 1 (Harus Pasar-01): {st.pop()}")
    print(f"Pop 2 (Harus Gudang-01): {st.pop()}")
    print(f"Pop 3 (Harus Petani-01): {st.pop()}")
    print(f"Pop 4 (Harus None/Underflow): {st.pop()}")
    print(f"Uji Kosong Akhir: {st.is_empty()}")

if __name__ == "__main__":
=======
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from data_structures.stack import Stack

def run_test():
    print("--- TESTING STACK (POINTER BASED) ---")
    st = Stack()
    
    # KOREKSI: Gunakan method is_empty(), jangan akses st.items
    print(f"Uji Kosong Awal: {st.is_empty()}") 
    
    st.push("Lokasi-Petani-01")
    st.push("Lokasi-Gudang-01")
    st.push("Lokasi-Pasar-01")
    print(f"Uji Kosong Setelah Push: {st.is_empty()}")
    
    print(f"Pop 1 (Harus Pasar-01): {st.pop()}")
    print(f"Pop 2 (Harus Gudang-01): {st.pop()}")
    print(f"Pop 3 (Harus Petani-01): {st.pop()}")
    print(f"Pop 4 (Harus None/Underflow): {st.pop()}")
    print(f"Uji Kosong Akhir: {st.is_empty()}")

if __name__ == "__main__":
>>>>>>> da21a552cb6396e3871768eb1a2dfb6377a563a4
    run_test()