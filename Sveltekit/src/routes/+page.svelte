<script lang="ts">
  import type { PageData } from './$types';
  import { enhance } from '$app/forms';
  
  export let data: PageData;
  export let form;

  </script>
<form method="POST" style="display: flex; flex-direction: column; align-items: flex-start; gap: 10px; margin-left: 24px" use:enhance>
  <div>
      <input name="name" type="text" placeholder="Name">
  </div>
  <div>
      <input name="description" type="text" placeholder="Description">
  </div>
    <button style="cursor: pointer;">Submit</button>
</form>
<p class="error">{form?.error || ""}</p>
  {#if data.error}
    <p>{data.error}</p>
  {:else if !data}
    <p>Loading...</p>
  {:else}
  <ol>
  {#each data.data as item}
    <li>{item.name} - {item.description}</li>
  {/each}
  </ol>
  {/if}