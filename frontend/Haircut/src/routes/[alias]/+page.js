// Make a request to the server as soon as the page is loaded using the alias parameter
// The alias parameter is the name of the page that we want to load
// The correct url is returned by the server in JSON format
// The server is running on port 8000

import { redirect } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';

export async function load({ params }) {
        let response = null;
        try {
            response = await fetch(`http://127.0.0.1:8000/${params.alias}/`);
        }
        catch (error) {
            console.error(error);
        }
        if (response !== null) {
            const data = await response.json();
            let url = null;
            if ("url" in data) {
                ({url} = data);
            }
            if (url !== null) {
                return redirect(302, url);
            }
        }
        error(404, 'Page not found');
}