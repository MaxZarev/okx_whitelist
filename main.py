# Чтение списка кошельков из текстового файла
with open('wallets.txt', 'r') as file:
    wallet_list = file.read().splitlines()

# Разделение кошельков на группы по 20
wallet_groups = [wallet_list[i:i + 20] for i in range(0, len(wallet_list), 20)]

# Создание строк с перечислением кошельков
formatted_wallets = []
for group in wallet_groups:
    formatted_group = '", "'.join(group)
    formatted_wallets.append(f'''
     
(function() {{
  const wallets = ["{formatted_group}"];
  
  const names = [];
  
  const walletSelectors = [];
  const nameSelectors = [];
  
  for (let i = 3; i <= 98; i += 5) {{
   walletSelectors.push(
     `#scroll-box > div > form > div:nth-child(3) > div > div > div > div > div:nth-child(${{i}}) > div.okui-form-item-control > div > div > div > div > input`
   );
  }}
  
  for (let i = 5; i <= 100; i += 5) {{
   nameSelectors.push(
     `#scroll-box > div > form > div:nth-child(3) > div > div > div > div > div:nth-child(${{i}}) > div.okui-form-item-control > div > div > div > div > input`
   );
  }}
  
  const addButtonSelector =
    "#scroll-box > div > form > div:nth-child(3) > div > div > div > div > div.add-address-form-btn";
  
  function fillInput(input, value) {{
    input.setAttribute('value', value);
    input.dispatchEvent(new Event('input', {{ bubbles: true }}));
  }}
  
  async function addWallets() {{
    for (let i = 0; i < wallets.length; i++) {{
      console.log(`Добавление кошелька ${{i + 1}} из ${{wallets.length}}`);
  
      const addressInput = document.querySelector(walletSelectors[i]);
      const nameInput = document.querySelector(nameSelectors[i]);
  
      fillInput(addressInput, wallets[i]);
      await new Promise((resolve) => setTimeout(resolve, 300));
  
      if (names.length > 0) {{
        fillInput(nameInput, names[i]);
        await new Promise((resolve) => setTimeout(resolve, 400));
      }}
  
      if (i < wallets.length - 1) {{
        const button = document.querySelector(addButtonSelector);
        button.click();
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }}
    }}
  
    console.log('Завершено');
  }}
  
  addWallets();
 }})();
****************************************************************************************************************************
''')

# Сохранение строк с перечислением кошельков в текстовый файл
with open('result.txt', 'w') as file:
    for wallets in formatted_wallets:
        file.write(wallets + '\n')
