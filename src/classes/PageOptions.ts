export default class PageOptions {
  title: string;
  menuVisible: boolean;

  constructor({ title, menuVisible }: { title: string; menuVisible: boolean }) {
    this.title = title;
    this.menuVisible = menuVisible;
  }
}
