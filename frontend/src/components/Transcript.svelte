<script lang="ts">
  import type { WhisperResult } from "../types/WhisperResult";
  import { getContent } from "../utils/convert";
  import { download } from "../utils/utils";
  import Button from "./Button.svelte";

  export let result: WhisperResult;
  export let duration: number;
  export let inputFileName: string;

  function formatTimestamp(n: number) {
    const seconds = Math.round(n % 60);
    const minutes = Math.floor(n / 60);

    return `${minutes.toString().padStart(2, "0")}:${seconds
      .toString()
      .padStart(2, "0")}`;
  }

  let fileType: "txt" | "vtt" | "srt" | "tsv" | "json" = "txt";
</script>

<hr class="my-6" />

<div class="flex justify-between items-center mb-6">
  <div>
    <h2 class="text-2xl font-bold mb-2">Transcription Result</h2>
    <p>
      Transcribed {result.text.split(" ").length} words in {formatTimestamp(
        duration / 1000,
      )}
    </p>
  </div>
  <div class="flex gap-2 h-min">
    <select class="dark:bg-gray-700 dark:text-white" bind:value={fileType}>
      <option value="txt">Plain text</option>
      <option value="vtt">VTT</option>
      <option value="srt">SRT</option>
      <option value="tsv">TSV</option>
      <option value="json">JSON</option>
    </select>

    <Button
      variant="flat"
      on:click={() =>
        download(inputFileName + "." + fileType, getContent(result, fileType))}
    >
      Download
    </Button>
  </div>
</div>

<div class="grid gap-2 grid-cols-[auto,1fr]">
  {#each result.segments as segment}
    <span class="font-medium text-gray-500 dark:text-gray-400 select-none"
      >{formatTimestamp(segment.start)}</span
    >
    <span>{segment.text}</span>
  {/each}
</div>
