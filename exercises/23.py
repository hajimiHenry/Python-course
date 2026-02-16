contacts = {}  # 用于存储联系人信息：name -> phone

while True:
    print("\n" + "=" * 20)
    print("通讯录管理系统")
    print("1. 添加联系人")
    print("2. 查找联系人")
    print("3. 删除联系人")
    print("4. 显示所有联系人")
    print("5. 退出程序")
    print("=" * 20)
    
    while True:
     
        choice = input("请输入功能序号: ")
    
        if choice in('1','2','3','4','5'):
            break 
        
        print("输入无效，请输入 1~5")

    if choice == "1":
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        contacts[name] = phone
        print(f"已添加联系人: {name}")
    elif choice == "2":
        found = False
        query_name = input("请输入要查找的姓名: ")
        for name in contacts:
            if query_name == name:
                found = True
                print(f"姓名对应的电话号码是：{contacts[name]}")
                break

        if not found :
            print("未找到联系人")
            
    elif choice =="3":
        delete = False  
        delete_name= input("请输入你想删除的联系人")
        for name in contacts:
            if delete_name == name:
                delete = True
                removed = contacts.pop(delete_name, None)
                print(f"已删除联系人{name}")
                break
        if not delete  :
            print("未找到要删除的联系人")
    
    elif choice == "4":
        show_all = contacts.items()
        for name, num in show_all:
            print(f"{name}:{num}")
    
    elif choice == "5":
        break