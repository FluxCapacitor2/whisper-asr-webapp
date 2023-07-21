<script lang="ts">
  import { fileSize } from "../utils/utils";
  import Spinner from "./Spinner.svelte";

  export let id: string;
  export let name: string;

  export let model: string;
  export let models: Promise<{ [key: string]: boolean }>;

  let size: number;

  models.then((data) => {
    if (data[id] === false) {
      fetch(`http://localhost:8000/size?model=${id}`)
        .then((res) => res.json())
        .then((modelSize) => (size = modelSize));
    }
  });
</script>

<div class="w-full h-full flex-1">
  <input
    type="radio"
    name="model"
    bind:group={model}
    value={id}
    {id}
    class="peer sr-only"
  />
  <label
    class="border hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors w-full h-full border-gray-300 cursor-pointer peer-checked:bg-gray-200 dark:peer-checked:bg-gray-700 rounded-md p-4 flex flex-col gap-2 items-center relative"
    for={id}
  >
    {#if $$slots.default}
      <div class="[&>*]:w-12 [&>*]:h-12 fill-gray-800 dark:fill-gray-300">
        <slot />
      </div>
    {/if}
    <h3 class="text-2xl font-bold">
      {name}
    </h3>
    <p class="text-xs text-gray-500 dark:text-gray-400">
      {#await models}
        <Spinner size={16} />
      {:then models}
        {#if models[id]}
          ✅ Downloaded
        {:else if size}
          {fileSize(size)} download
        {:else}
          <Spinner size={16} />
        {/if}
      {/await}
    </p>
  </label>
</div>
