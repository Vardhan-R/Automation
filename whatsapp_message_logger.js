s = ""
i = 0

while (true) {
    try {
        s += $x("/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[" + String(i) + "]/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span")[0].innerText + '\n'
    } catch (error) {
        try {
            s += $x("/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[" + String(i) + "]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/span")[0].innerText + '\n'
        } catch (error) {
            try {
                s += $x("/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[" + String(i) + "]/div/div/div/div[2]/div[1]/div[2]/div/span[1]/span")[0].innerText + '\n'
            } catch (error) {
                try {
                    s += $x("/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[" + String(i) + "]/div/div/div/div[1]/div[1]/div[2]/div[2]/span[1]/span")[0].innerText + '\n'
                } catch (error) {
                    try {
                        s += $x("/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[" + String(i) + "]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span/img")[0].alt + '\n'
                    } catch (error) {
                        if (i > 100) {
                            console.log(i)
                            break
                        }
                    }
                }
            }
        }
    }
    i++
}

console.log(s)

// /html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[16]/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span
// /html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[16]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/span[1]/span
// /html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[26]/div/div/div/div[1]/div[1]/div[2]/div[2]/span[1]/span
// /html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[34]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/span/img