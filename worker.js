addEventListener('fetch', event => {
event.respondWith(doRedirects(event.request))
})
const newLocationHost = "developers.cloudflare.com/workers/about";

async function doRedirects(request) {
 let reqUA = request.headers.get("User-Agent")
 console.log(reqUA)
 let reqCK = request.headers.get("cf-noredir")
 console.log(reqCK)
 if (reqCK && reqCK.match('true'))
    return fetch(request)
 else if (reqUA.match('curl')) {
    let newLocation = "https://"+newLocationHost
 return Response.redirect(newLocation, 302)
 }
return fetch(request);
}
