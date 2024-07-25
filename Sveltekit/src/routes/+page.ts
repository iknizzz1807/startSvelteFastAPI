import type { PageLoad } from "./$types";

export const load = (async ({ fetch }) => {
  let data: any = null;
  let error: string | null = null;
  try {
    const response = await fetch("http://localhost:8000/items");
    if (response.ok) {
      data = await response.json();
    } else {
      error = `Error: ${response.status}`;
    }
  } catch (err) {
    error = `Error: ${(err as Error).message}`;
  }
  return {
    data,
    error,
  };
}) satisfies PageLoad;
