import os
import json
import requests
import mysql.connector
from tabulate import tabulate

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="db_akademik_0561"
)

if db.is_connected():
    print()
    print('Database is opened successfully!!!')
    print()

def fetchnstore():
	url = "https://api.abcfdab.cfd/students"
	res = requests.get(url)
	parsing =  json.loads(res.text)
	hasil = parsing['data']
	cur = db.cursor()
	sql = "INSERT INTO tbl_students_0561 (id, nim, nama, jk, jurusan, alamat) VALUES (%s, %s, %s, %s, %s, %s)" 
	for row in hasil:
		data = (row['id'],row['nim'],row['nama'],row['jk'],row['jurusan'],row['alamat'])
		cur.execute(sql,data)
	db.commit()
	print("[Successfully Uploaded]\n")

def show_all():
	cur = db.cursor()
	sql = "SELECT * FROM tbl_students_0561"
	cur.execute(sql)
	res = cur.fetchall()
	print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))

def with_limit():
	try:
		cur = db.cursor()
		number = int(input("Masukkan Limit : "))
		sql = "SELECT * FROM tbl_students_0561 LIMIT %s" % (number)
		cur.execute(sql)
		res = cur.fetchall()
		print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
	except:
		print("\n[Data entered incorrectly!]\n")

def with_nim():
	try:
		cur = db.cursor()
		value = input("Masukkan NIM : ")
		sql = "SELECT * FROM tbl_students_0561 WHERE nim = '%s'" % (value)
		cur.execute(sql)
		res = cur.fetchall()
		if not res:
			print(f"Data {value} is not found!")
			print(tabulate([["NA","NA","NA","NA","NA","NA"]], headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
		else:
			print(f"Data {value} ditemukan!")
			print(tabulate(res,headers=["NO","NIM","Nama","JK","Jurusan","Alamat"],tablefmt='pretty'))
	except:
		print("\n[Data entered incorrectly]\n")
		

def menu():
	print(f"""
    {'='*50}
    ={('Program API').center(48)}=
    {'='*50}
    """)
	print("1. Tampilkan semua data")
	print("2. Tampilkan data berdasarkan limit")
	print("3. Cari data berdasarkan NIM")
	print("0. Keluar")
	print()

def main():
	while True:
		menu()
		pilihan = int(input("Pilih menu>> "))
		if pilihan == 1:
			show_all()
		elif pilihan == 2:
			os.system('cls')
			with_limit()
		elif pilihan == 3:
			os.system('cls')
			with_nim()
		elif pilihan == 0:
			break
		else:
			print("\n[Data entered incorrectly !]\n")
		

if __name__ == '__main__':
	# fetchnstore()
	main()
	