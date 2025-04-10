
# key chính, muốn thực hiện cái nào thì nhập vào đây, có thể nhập từ cái, vd: "faucet", "teko_faucet" hoặc nhập KEY chính là được vd: FAUCET vì key này đã bao gồm "faucet", "teko_faucet"
# khi key này thay đổi, để apply vào bot cần chạy lại [3] 💾 Database actions => [4] 🔄 Regenerate Tasks for All Wallets
TASKS = ["CRUSTY_SWAP","CAP_APP","BEBOP","GTE_SWAPS","TEKO_FINANCE","ONCHAIN_GM","XL_MEME","OMNIHUB", "MINTAIR","EASYNODE","HOPNETWORK","RAINMAKR"]

FAUCET = ["faucet"]

CRUSTY_SWAP = [
    # "cex_withdrawal",
    "crusty_refuel",
    # "crusty_refuel_from_one_to_all",
]

CAP_APP = ["cap_app"]
BEBOP = ["bebop"]
GTE_SWAPS = ["gte_swaps"]
TEKO_FINANCE = ["teko_faucet", "teko_finance"]
ONCHAIN_GM = ["onchain_gm"]
XL_MEME = ["xl_meme"]
OMNIHUB = ["omnihub"]
MINTAIR = ["mintair"]
EASYNODE = ["easynode"]
HOPNETWORK = ["hopnetwork"]
RAINMAKR = ["rainmakr"]

"""===========Hướng dẫn sử dụng | Guild ===========
VN:
Bạn có thể tạo tác vụ của riêng mình với các mô-đun mà bạn cần
và thêm nó vào danh sách TASKS hoặc sử dụng các tác vụ đã được thiết lập sẵn của chúng tôi.

( ) - Có nghĩa là tất cả các mô-đun bên trong dấu ngoặc sẽ được thực hiện
theo thứ tự ngẫu nhiên
[ ] - Có nghĩa là chỉ một trong các mô-đun bên trong dấu ngoặc sẽ được thực hiện
ngẫu nhiên

XEM VÍ DỤ DƯỚI ĐÂY:

TASKS = [
    "CREATE_YOUR_OWN_TASK",
]
CREATE_YOUR_OWN_TASK = [
    "faucet",
    ("faucet_tokens", "swaps"),
    ["storagescan_deploy", "conft_mint"],
    "swaps",
]

DƯỚI ĐÂY LÀ CÁC TÁC VỤ ĐÃ ĐƯỢC THỰC HIỆN SẴN MÀ BẠN CÓ THỂ SỬ DỤNG:

crusty_refuel - nạp MEGAETH tại https://www.crustyswap.com/
crusty_refuel_from_one_to_all - share MEGAETH tới các ví khác 
cex_withdrawal - rút ETH từ sàn giao dịch cex (okx, bitget)
faucet - nhận mega eth tokens (cần captcha)
cap_app - mint cUSD tại https://cap.app/testnet
bebop - giao dịch token tại https://bebop.xyz/trade?network=megaeth&sell=ETH
gte_swaps - giao dịch token tại https://testnet.gte.xyz/
teko_finance - stake tkUSDC tại https://app.teko.finance/
onchain_gm - mint GM tại https://onchaingm.com/
xl_meme - mua memetokens tại https://testnet.xlmeme.com/megaeth
omnihub - mint NFT tại https://omnihub.xyz/collections?chain=megaeth-testnet&sort_by=trending
mintair - deploy timer contract tại https://contracts.mintair.xyz/
easynode - deploy counter contract tại https://playground.easy-node.xyz/
hopnetwork - tham gia danh sách chờ tại https://hopnetwork.xyz/
owlto - deploy basic contract tại https://owlto.finance/deploy/?chain=MegaTestnet
rainmakr - mua meme token tại https://rainmakr.xyz/en/rainai

--------------------------------
EN:
You can create your own task with the modules you need 
and add it to the TASKS list or use our ready-made preset tasks.

( ) - Means that all of the modules inside the brackets will be executed 
in random order
[ ] - Means that only one of the modules inside the brackets will be executed 
on random
SEE THE EXAMPLE BELOW:

RU:
Вы можете создать свою задачу с модулями, которые вам нужны, 
и добавить ее в список TASKS, см. пример ниже:

( ) - означает, что все модули внутри скобок будут выполнены в случайном порядке
[ ] - означает, что будет выполнен только один из модулей внутри скобок в случайном порядке
СМОТРИТЕ ПРИМЕР НИЖЕ:

CHINESE:
你可以创建自己的任务，使用你需要的模块，
并将其添加到TASKS列表中，请参见下面的示例：

( ) - 表示括号内的所有模块将按随机顺序执行
[ ] - 表示括号内的模块将按随机顺序执行

--------------------------------
!!! IMPORTANT !!!
EXAMPLE | ПРИМЕР | 示例:

TASKS = [
    "CREATE_YOUR_OWN_TASK",
]
CREATE_YOUR_OWN_TASK = [
    "faucet",
    ("faucet_tokens", "swaps"),
    ["storagescan_deploy", "conft_mint"],
    "swaps",
]
--------------------------------


BELOW ARE THE READY-MADE TASKS THAT YOU CAN USE:
СНИЗУ ПРИВЕДЕНЫ ГОТОВЫЕ ПРИМЕРЫ ЗАДАЧ, КОТОРЫЕ ВЫ МОЖЕТЕ ИСПОЛЬЗОВАТЬ:
以下是您可以使用的现成任务：


crusty_refuel - refuel MEGAETH at https://www.crustyswap.com/
crusty_refuel_from_one_to_all - refuel MEGAETH from one to all wallets at https://www.crustyswap.com/
cex_withdrawal - withdraw ETH from cex exchange (okx, bitget)
faucet - faucet mega eth tokens (needs captcha)
cap_app - mint cUSD at https://cap.app/testnet
bebop - trade tokens at https://bebop.xyz/trade?network=megaeth&sell=ETH
gte_swaps - trade tokens at https://testnet.gte.xyz/
teko_finance - stake tkUSDC at https://app.teko.finance/
onchain_gm - mint GM at https://onchaingm.com/
xl_meme - buy memetokens at https://testnet.xlmeme.com/megaeth
omnihub - mint NFT at https://omnihub.xyz/collections?chain=megaeth-testnet&sort_by=trending
mintair - deploy timer contract at https://contracts.mintair.xyz/
easynode - deploy counter contract at https://playground.easy-node.xyz/
hopnetwork - join waitlist at https://hopnetwork.xyz/
owlto - deploy basic contract at https://owlto.finance/deploy/?chain=MegaTestnet
rainmakr - buy meme token at https://rainmakr.xyz/en/rainai
"""
