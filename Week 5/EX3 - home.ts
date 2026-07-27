import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html'
})
export class HomeComponent {

  name = "Aishwarya";

  imageUrl = "https://via.placeholder.com/150";

  count = 0;

  increase() {
    this.count++;
  }

}
