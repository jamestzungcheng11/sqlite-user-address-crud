import sqlite3
import model
import json 

def create_connection(db_file):
  try:
     conn=sqlite3.connect(db_file)
     return conn 
  except sqlite3.Error as e:
    print(f"Error ao conectar: {e}")
    return None 


def get_user_with_addresses(conn,user_id):
  try:
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM users WHERE id = ? ",(user_id,))
    user=cursor.fetchone()
   
    
    cursor.execute("SELECT * FROM addresses WHERE user_id = ? ",(user_id,))
    addresses=cursor.fetchall()
    user_data={
         "id":user[0],
         "first_name":user[1],
         "last_name":user[2],
          "email":user[3],
          "addresses":[]
    }

    for addr in addresses:
       address_data={
            "id":addr[0],
            "street":addr[2],
            "zip_code":addr[4],
            "latitude":addr[5],
            "longitude":addr[6]
       }
       user_data["addresses"].append(address_data)


    return user_data 
  except sqlite3.Error as e:
       print(f"Erro ao buscar os dados {e}")
       return None 

  




def save_to_json(data,file_name):
    try:
      with open(file_name ,"w", encoding="utf-8") as f:
          json.dump(data,f,ensure_ascii=False,indent=4)
          print(f"Arquivo salvo {file_name}")
    except Exception as e:
      print(f"Erro ao salvar o json {e}")



   