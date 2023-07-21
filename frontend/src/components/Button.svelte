<script lang="ts">
  import clsx from "clsx";
  import Spinner from "./Spinner.svelte";

  export let loading = false;
  export let variant: "primary" | "flat";
</script>

<button
  on:click
  class={clsx(
    variant === "primary" &&
      "bg-primary-700 hover:bg-primary-800 active:bg-primary-900",
    variant === "flat" &&
      "bg-neutral-700 hover:bg-neutral-800 active:bg-neutral-900 border border-neutral-600 dark:border-neutral-400",
    "text-white rounded-md px-3 py-2 transition-colors flex items-center justify-center gap-2",
  )}
>
  {#if loading}
    <Spinner size={18} color="#fff" />
  {/if}
  <slot />
</button>
