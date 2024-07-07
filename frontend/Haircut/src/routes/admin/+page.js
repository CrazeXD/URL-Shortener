import { redirect } from '@sveltejs/kit';

export async function load() {
    return redirect(302, 'http://127.0.0.1:8000/admin/' );
}