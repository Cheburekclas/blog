function showActiveLink(menu){
    try {
        const url = document.location.href
        const links = document.getElementById(menu).querySelectorAll('a')
        for(const link of links){
            if (link.href === url){
                link.classList.add('active')
            }
        }
    } catch (error) {
        console.log(error)
    }
}
showActiveLink('menu')