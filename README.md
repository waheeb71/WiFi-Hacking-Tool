
```markdown
# WiFi Hacking Tool

![GitHub](https://img.shields.io/github/license/waheeb71/WiFi-Hacking-Tool?color=green)
![GitHub last commit](https://img.shields.io/github/last-commit/waheeb71/WiFi-Hacking-Tool)

WiFi Hacking Tool is a powerful Python-based tool designed for ethical hacking and network analysis. It provides a user-friendly interface to capture handshakes, crack passwords, analyze network traffic, and perform various network attacks.

## Features:
- **Handshake Capture:** Capture WPA/WPA2 handshakes from target networks.
- **Password Cracking:** Use wordlists or custom dictionaries to crack captured handshakes.
- **Network Monitoring:** Enter monitor mode and analyze nearby networks.
- **Deauthentication Attacks:** Disconnect devices from a network or target specific devices.
- **Traffic Analysis:** Analyze network traffic using BetterCAP.

## Requirements:
- **Operating System:** Kali Linux or any Debian-based distribution.
- **Python Version:** Python 3.x
- **Required Packages:**
  - `bettercap`
  - `aircrack-ng`
  - `iw`
  - `termcolor`
  - `subprocess`

## Installation:

### Step 1: Clone the Repository
```bash
git clone https://github.com/waheeb71/WiFi-Hacking-Tool.git
cd WiFi-Hacking-Tool
```

### Step 2: Install Dependencies
Run the following command to install the required packages:
```bash
sudo apt update
sudo apt install bettercap aircrack-ng iw python3-pip
pip3 install termcolor
```

### Step 3: Run the Tool
```bash
python3 wifi_haker.py
```

## Usage:
1. **Capture Handshake:** Select option `1` to capture handshakes from nearby networks.
2. **Crack Passwords:** Use option `4` to crack captured handshakes with a wordlist.
3. **Monitor Networks:** Enter monitor mode using option `3`.
4. **Disconnect Devices:** Perform deauthentication attacks using options `5` or `6`.



### **Detailed Explanation of Functions and How to Use Them:**

#### **1. Capturing the Handshake (`Capture Handshake`):**
- **Description:**  
  This function allows you to capture the "Handshake" (the initial connection process) between a client device and a wireless network. This is done by targeting a specific Wi-Fi network and forcing one of the connected devices to reconnect, allowing you to capture the encrypted handshake data.

- **How to Use:**
  1. Select option `1` from the main menu.
  2. Enter the name of the wireless interface (e.g., `wlan0`).
  3. The tool will start scanning for nearby networks.
  4. Select the target network and enter its channel number (Channel).
  5. The handshake will be captured and saved in a file (usually with a `.cap` extension).

- **Importance of the Handshake:**  
  The handshake is part of the connection process between the client and the network, containing encrypted data that can later be used to attempt cracking the password.

---

#### **2. Cracking Passwords Using a Wordlist (`Crack Passwords`):**
- **Description:**  
  After capturing the handshake, you can use this function to attempt to crack the network's password using a wordlist. A wordlist is a file containing a collection of possible passwords.

- **How to Use:**
  1. Select option `4` from the main menu.
  2. Enter the name of the previously captured handshake file (without the `.cap` extension).
  3. Choose whether to use a default wordlist (like `rockyou.txt`) or provide the path to your custom wordlist.
  4. The tool will start attempting to match passwords from the list with the captured handshake.
  5. If successful, the password will be displayed.

- **Note:**  
  You should have a strong and diverse wordlist to increase the chances of success. Tools like `crunch` can be used to generate custom wordlists.

---

#### **3. Entering Monitor Mode (`Monitor Networks`):**
- **Description:**  
  Monitor mode is a special mode for wireless interfaces that allows you to "listen" to all packets being sent and received over the network, even if you're not connected to it. This mode is essential for performing various attacks, such as capturing handshakes or deauthentication attacks.

- **How to Use:**
  1. Select option `3` from the main menu.
  2. Enter the name of the wireless interface (e.g., `wlan0`).
  3. The tool will switch the interface to monitor mode (usually changing the interface name to something like `wlan0mon`).

- **Importance of Monitor Mode:**  
  Without monitor mode, you won't be able to capture wireless packets or perform network analysis-based attacks.

---

#### **4. Disconnecting Devices from the Network (`Disconnect Devices`):**
- **Description:**  
  This function allows you to perform **Deauthentication** attacks, which aim to temporarily disconnect devices from a Wi-Fi network. These attacks can be used to capture handshakes or disrupt connected devices.

- **How to Use:**
  - There are two types of attacks:
    1. **Disconnect All Devices from the Network:**
       - Select the appropriate option from the submenu.
       - Enter the MAC address of the network (BSSID) and the wireless interface name.
       - Specify the duration of the attack (in seconds) or leave it as `0` for a continuous attack.
    2. **Disconnect a Specific Device:**
       - Enter the MAC address of the target device and the MAC address of the network (BSSID).
       - Specify the duration of the attack (in seconds).

- **Importance of the Attack:**  
  This type of attack can be used to capture handshakes or force devices to reconnect to the network, making it easier to execute other attacks.

---

## **How to Use a WiFi Adapter for Wi-Fi Networks:**

To perform the operations described above, you'll need a **WiFi Adapter** that supports **Monitor Mode** and **Packet Injection**. Here are the steps:

### **1. Choosing a Suitable WiFi Adapter:**
- The WiFi adapter you use should support:
  - **Monitor Mode:** Allows you to listen to all wireless packets.
  - **Packet Injection:** Allows you to send custom packets to the network (such as deauthentication attacks).

- Examples of common WiFi adapters:
  - **Alfa AWUS036ACH**
  - **Alfa AWUS036NHA**
  - **Panda Wireless PAU09**

### **2. Installing Necessary Drivers:**
- If you're using Kali Linux, most WiFi adapters work well without needing additional drivers.
- If you encounter issues, you can install the necessary drivers using the following commands:
  ```bash
  sudo apt update
  sudo apt install realtek-rtl88xxau-dkms
  ```

### **3. Checking for Monitor Mode Support:**
- Run the following command to check if your WiFi adapter supports monitor mode:
  ```bash
  iw list | grep "Supported interface modes" -A 8
  ```
- If "Monitor" appears in the list, it means your WiFi adapter supports monitor mode.

### **4. Enabling Monitor Mode:**
- Use the following command to switch the interface to monitor mode:
  ```bash
  sudo airmon-ng start wlan0
  ```
- You'll notice that the interface name changes to something like `wlan0mon`.

### **5. Using the WiFi Adapter with the Tool:**
- When running the tool, make sure to enter the correct interface name (e.g., `wlan0mon` if you're in monitor mode).
- You can now use the tool to perform the operations described above.

---

## **Important Notes:**
1. **Ethical Use Only:**  
   This tool should only be used for educational and ethical purposes. Do not attempt to hack into networks without explicit permission.

2. **Local Laws:**  
   Ensure that your use of this tool complies with local laws in your country.

3. **Test on Your Own Network:**  
   Always test the tool on your own network or networks where you have explicit permission to conduct tests.


## Screenshots:
![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)
![Screenshot 3](screenshots/screenshot3.png)
![Screenshot 4](screenshots/screenshot4.png)
![Screenshot 5](screenshots/screenshot5.png)

## Disclaimer:
This tool is intended for educational and ethical purposes only. Unauthorized use of this tool on networks you do not own is illegal. The developer is not responsible for any misuse of this tool.

## Contact:
For questions or support, contact me via:
- Telegram: [@SyberSc71](https://t.me/SyberSc71)
- GitHub: [waheeb71](https://github.com/waheeb71)

## License:
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
```

## **شرح الاستخدامات بالعربي:**

### **1. التقاط الـ Handshake (`Capture Handshake`):**
- **الوصف:**  
  هذه الوظيفة تتيح لك التقاط "Handshake" (المصافحة) بين جهاز العميل والشبكة اللاسلكية. يتم ذلك عن طريق استهداف شبكة Wi-Fi محددة وإجبار أحد الأجهزة المتصلة على إعادة الاتصال بالشبكة، مما يسمح لك بالحصول على بيانات الـ Handshake المشفرة.
  
- **كيفية الاستخدام:**
  1. اختر الخيار `1` من القائمة الرئيسية.
  2. قم بإدخال اسم واجهة الشبكة اللاسلكية (مثل `wlan0`).
  3. ستبدأ الأداة في البحث عن الشبكات القريبة.
  4. حدد الشبكة المستهدفة وأدخل رقم القناة (Channel) الخاص بها.
  5. سيتم التقاط الـ Handshake وحفظه في ملف (عادة بصيغة `.cap`).

- **أهمية الـ Handshake:**  
  الـ Handshake هو جزء من عملية الاتصال بين العميل والشبكة، ويحتوي على بيانات مشفرة يمكن استخدامها لاحقًا لمحاولة كسر كلمة المرور.

---

### **2. كسر كلمات السر باستخدام قائمة كلمات (`Crack Passwords`):**
- **الوصف:**  
  بعد التقاط الـ Handshake، يمكنك استخدام هذه الوظيفة لمحاولة كسر كلمة مرور الشبكة باستخدام قائمة كلمات (Wordlist). قائمة الكلمات عبارة عن ملف يحتوي على مجموعة من كلمات المرور المحتملة.

- **كيفية الاستخدام:**
  1. اختر الخيار `4` من القائمة الرئيسية.
  2. أدخل اسم ملف الـ Handshake الذي تم التقاطه مسبقًا (بدون الامتداد `.cap`).
  3. اختر ما إذا كنت تريد استخدام قائمة كلمات افتراضية (مثل `rockyou.txt`) أو إدخال مسار ملف خاص بك.
  4. ستبدأ الأداة في محاولة مطابقة كلمات المرور من القائمة مع الـ Handshake.
  5. إذا نجحت العملية، سيتم عرض كلمة المرور.

- **ملحوظة:**  
  يجب أن تكون لديك قائمة كلمات قوية ومتنوعة لزيادة فرص النجاح. يمكنك استخدام أدوات مثل `crunch` لإنشاء قوائم كلمات مخصصة.

---

### **3. الدخول إلى وضع المراقبة (`Monitor Networks`):**
- **الوصف:**  
  وضع المراقبة (Monitor Mode) هو وضع خاص بواجهات الشبكة اللاسلكية يتيح لك "الاستماع" إلى جميع الحزم التي يتم إرسالها واستقبالها عبر الشبكة، حتى لو لم تكن متصلًا بها. هذا الوضع ضروري لتنفيذ العديد من الهجمات مثل التقاط الـ Handshake أو هجمات فصل الأجهزة.

- **كيفية الاستخدام:**
  1. اختر الخيار `3` من القائمة الرئيسية.
  2. أدخل اسم واجهة الشبكة اللاسلكية (مثل `wlan0`).
  3. ستقوم الأداة بتحويل الواجهة إلى وضع المراقبة (عادةً سيتغير اسم الواجهة إلى شيء مثل `wlan0mon`).

- **أهمية وضع المراقبة:**  
  بدون وضع المراقبة، لن تتمكن من التقاط الحزم اللاسلكية أو تنفيذ الهجمات التي تعتمد على تحليل الشبكة.

---

### **4. فصل الأجهزة عن الشبكة (`Disconnect Devices`):**
- **الوصف:**  
  هذه الوظيفة تتيح لك تنفيذ هجمات **Deauthentication** (فصل الاتصال)، وهي هجمات تهدف إلى فصل الأجهزة المتصلة بشبكة Wi-Fi عن الشبكة مؤقتًا. يمكن استخدام هذا النوع من الهجمات لالتقاط الـ Handshake أو لإزعاج الأجهزة المتصلة.

- **كيفية الاستخدام:**
  - هناك نوعان من الهجمات:
    1. **فصل جميع الأجهزة عن الشبكة:**
       - اختر الخيار المناسب من القائمة الفرعية.
       - أدخل عنوان MAC الخاص بالشبكة (BSSID) واسم واجهة الشبكة.
       - حدد مدة الهجوم (بالثواني) أو اتركها `0` لجعل الهجوم مستمرًا.
    2. **فصل جهاز معين عن الشبكة:**
       - أدخل عنوان MAC للجهاز المستهدف وعنوان MAC للشبكة (BSSID).
       - حدد مدة الهجوم (بالثواني).

- **أهمية الهجوم:**  
  يمكن استخدام هذا النوع من الهجمات لالتقاط الـ Handshake أو لإجبار الأجهزة على إعادة الاتصال بالشبكة، مما يسهل عليك تنفيذ الهجمات الأخرى.

---

## **كيفية استخدام WiFi Adapter لشبكة Wi-Fi:**

لتنفيذ العمليات المذكورة أعلاه، ستحتاج إلى **WiFi Adapter** يدعم وضع المراقبة (Monitor Mode) وهجمات الحقن (Packet Injection). إليك الخطوات:

### **1. اختيار WiFi Adapter مناسب:**
- يجب أن يكون الـ WiFi Adapter الذي تستخدمه يدعم:
  - **وضع المراقبة (Monitor Mode):** يتيح لك الاستماع إلى جميع الحزم اللاسلكية.
  - **حقن الحزم (Packet Injection):** يتيح لك إرسال حزم مخصصة إلى الشبكة (مثل هجمات Deauthentication).

- أمثلة على WiFi Adapters شائعة:
  - **Alfa AWUS036ACH**
  - **Alfa AWUS036NHA**
  - **Panda Wireless PAU09**

### **2. تثبيت التعريفات اللازمة:**
- إذا كنت تستخدم نظام Kali Linux، فإن معظم الـ WiFi Adapters تعمل بشكل جيد دون الحاجة إلى تثبيت تعريفات إضافية.
- إذا كنت تواجه مشاكل، يمكنك تثبيت التعريفات باستخدام الأوامر التالية:
  ```bash
  sudo apt update
  sudo apt install realtek-rtl88xxau-dkms
  ```

### **3. التحقق من دعم وضع المراقبة:**
- قم بتشغيل الأمر التالي للتحقق مما إذا كان الـ WiFi Adapter يدعم وضع المراقبة:
  ```bash
  iw list | grep "Supported interface modes" -A 8
  ```
- إذا ظهر "Monitor" في القائمة، فهذا يعني أن الـ WiFi Adapter يدعم وضع المراقبة.

### **4. تشغيل وضع المراقبة:**
- استخدم الأمر التالي لتحويل الواجهة إلى وضع المراقبة:
  ```bash
  sudo airmon-ng start wlan0
  ```
- ستلاحظ أن اسم الواجهة قد تغير إلى `wlan0mon`.

### **5. استخدام الـ WiFi Adapter مع الأداة:**
- عند تشغيل الأداة، تأكد من إدخال اسم الواجهة الصحيحة (مثل `wlan0mon` إذا كنت في وضع المراقبة).
- يمكنك الآن استخدام الأداة لتنفيذ العمليات المذكورة أعلاه.

---

## **ملحوظات مهمة:**
1. **الأغراض الأخلاقية فقط:**  
   يجب استخدام هذه الأداة للأغراض التعليمية والأخلاقية فقط. لا تحاول اختراق شبكات لا تملك إذنًا بالوصول إليها.

2. **القوانين المحلية:**  
   تأكد من أن استخدامك لهذه الأداة يتوافق مع القوانين المحلية في بلدك.

3. **الاختبار على شبكتك الخاصة:**  
   دائمًا قم باختبار الأداة على شبكتك الخاصة أو شبكات حصلت على إذن صريح لاختبارها.

---
```

