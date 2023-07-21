<script lang="ts">
  import { fileSize } from "../utils/utils";
  import UploadIcon from "./UploadIcon.svelte";

  export let files: FileList;
</script>

<div class="flex items-center justify-center w-full">
  <label
    for="dropzone-file"
    class={`flex flex-col items-center justify-center w-full h-40 border-2 border-gray-300 border-dashed rounded-lg bg-gray-50 dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600 transition-colors ${
      (!files || files.length === 0) && "cursor-pointer"
    }`}
  >
    <div class="flex flex-col items-center justify-center pt-5 pb-6">
      <UploadIcon />
      <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
        {#if files?.length > 0}
          <span class="font-bold">{files?.item(0).name}</span>
          ({fileSize(files.item(0).size)})
        {:else}
          <span class="font-bold">Click to upload</span> or drag and drop
        {/if}
      </p>
      <p class="text-xs text-gray-500 dark:text-gray-400">
        {#if files?.length > 0}
          <button
            on:click={() => (files = undefined)}
            class="font-medium underline">Reset</button
          >
        {:else}
          Any FFmpeg-compatible audio file
        {/if}
      </p>
    </div>

    <input
      id="dropzone-file"
      type="file"
      class="hidden"
      disabled={files?.length > 0}
      bind:files
    />
  </label>
</div>
